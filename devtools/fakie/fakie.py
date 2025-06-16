import os
import json
import threading
import webbrowser
import inspect
import argparse

from enum import Enum
from faker import Faker
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

from devtools.fakie.CustomDataTypes import CustomDataTypes
from devtools.fakie.FakerDataTypes import FakerDataTypes
from devtools.fakie.customGenerators import generate_custom_phone_number

FRONTEND_DIR = os.path.join(os.path.dirname(__file__), "frontend")


def register(subparsers):
    parser = subparsers.add_parser(
        "fakie",
        help="Start Fakie server to mock data.",
        add_help=False,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("-h", "--help", action="help", default=argparse.SUPPRESS, help="Show help message.")
    parser.add_argument("--host", default="127.0.0.1", help="Host address to bind the server")
    parser.add_argument("--port", type=int, default=5000, help="Port number to bind the server")
    parser.add_argument("--debug", action="store_true", help="Run Flask in debug mode")
    parser.set_defaults(func=run)

def run(args):
    threading.Timer(0.1, lambda: webbrowser.open(f"http://{args.host}:{args.port}/")).start()

    app = create_app()
    app.run(host=args.host, port=args.port, debug=args.debug)


def create_app():
    """
    Creates and configures the Flask application.
    Sets up CORS, loads supported types, and defines API routes.
    """
    app = Flask(__name__, static_folder=FRONTEND_DIR)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    SUPPORTED_TYPES = build_supported_types()

    @app.route("/api/supported_types", methods=["GET"])
    def get_supported_types():
        """
        Returns a list of supported data types.

        Returns:
            JSON: A dictionary containing supported types.
        """

        return jsonify(SUPPORTED_TYPES)

    @app.route("/api/generate_data", methods=["POST"])
    def generate_data():
        """
        Generates fake data based on a given structure, locale, and record count.

        Request JSON:
            {
                "structure": dict,          # Required. Field structure for fake data.
                "locale": str,              # Optional. Default is 'en_US'.
                "numRecords": int           # Optional. Default is 1.
            }

        Returns:
            JSON: A dictionary containing generated data or an error message.
        """

        payload = request.get_json() or {}
        structure = payload.get("structure")
        locale = payload.get("locale", "en_US")
        num_records = payload.get("numRecords", 1)

        if not isinstance(structure, dict):
            return jsonify({"error": "Invalid \"structure\" format"}), 400

        try:
            generated = generate_fake_data(structure, locale, num_records, SUPPORTED_TYPES)
            return jsonify({"data": generated})
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    @app.route("/api/exampleScheme", methods=["GET"])
    def get_data_structure():
        """
        Returns a sample data schema from the static 'exampleScheme.json' file.

        Returns:
            JSON: Example schema or an error if the file is not found.
        """

        schema_path = os.path.join(app.static_folder, "exampleScheme.json")
        try:
            with open(schema_path, "r") as f:
                return jsonify(json.load(f))
        except FileNotFoundError:
            return jsonify({"error": "exampleScheme.json not found"}), 404

    @app.route("/", defaults={"path": "index.html"})
    @app.route("/<path:path>")  # Fallback to "index.html" if route does not exist
    def serve_frontend(path):
        """
        Serves the frontend files. Defaults to 'index.html' for unknown paths.

        Args:
            path (str): Requested frontend path.

        Returns:
            HTML: The requested file or 'index.html' if not found.
        """

        full_path = os.path.join(app.static_folder, path)
        if os.path.isfile(full_path):
            return send_from_directory(app.static_folder, path)

        return send_from_directory(app.static_folder, "index.html")

    return app


def build_supported_types():
    """
    Scans the FakerDataTypes and CustomDataTypes classes for Enum subclasses,
    and constructs a dictionary of supported data types.

    Returns:
        dict: A dictionary mapping each Enum class name to a dict of its member names and values.
              Example: {"Personal": {"EMAIL": "email", "PHONE_NUMBER": "phone_number"}, ...}
    """

    supported = {}
    for cls in (FakerDataTypes, CustomDataTypes):
        for name, obj in inspect.getmembers(cls):
            if inspect.isclass(obj) and issubclass(obj, Enum):
                supported[name] = {m.name: m.value for m in obj}

    return supported


def generate_fake_data(structure, locale, count, supported_types):
    """
    Recursively generates a list of fake data records based on a user-defined structure.

    Args:
        structure (dict): Schema describing the structure and types of the data to generate.
        locale (str): Faker locale to use (e.g., 'en_US', 'fr_FR').
        count (int): Number of records to generate.
        supported_types (dict): Dictionary of supported types built by `build_supported_types`.

    Returns:
        list: A list of generated records, each conforming to the specified structure.

    Raises:
        ValueError: If an unsupported data type is encountered.
    """

    fake = Faker(locale)
    records = []

    for _ in range(count):
        record = {}
        for key, val in structure.items():
            if isinstance(val, dict):
                record[key] = generate_fake_data(val, locale, 1, supported_types)[0]
            elif isinstance(val, list):
                item_type = val[0]
                repeat = val[1] if len(val) > 1 else 1
                record[key] = [generate_value(item_type, fake, supported_types) for _ in range(repeat)]
            else:
                record[key] = generate_value(val, fake, supported_types)

        records.append(record)

    return records


def generate_value(data_type, fake, supported_types):
    """
    Resolves a data type to its corresponding Faker method or custom generator
    and returns a single generated value.

    Args:
        data_type (str): The name of the data type (e.g., "EMAIL", "FIRST_NAME").
        fake (Faker): An instance of the Faker class initialized with a locale.
        supported_types (dict): Dictionary of supported types built by `build_supported_types`.

    Returns:
        Any: A single generated value based on the specified data type.

    Raises:
        ValueError: If the data_type is not supported.
    """

    if data_type == CustomDataTypes.Personal.PHONE_NUMBER.name:
        return generate_custom_phone_number()

    for category in supported_types.values():
        if data_type in category:
            method_name = category[data_type].name
            method = getattr(fake, method_name, None)
            if callable(method):
                return method()

    raise ValueError(f"Unsupported data type: {data_type}")

