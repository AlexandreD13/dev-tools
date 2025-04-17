import argparse
from devtools import http_status, text_stats, color_converter
from colorama import init


def main(argv=None):
    init()

    parser = argparse.ArgumentParser(
        prog="devtools",
        description="A CLI tool.",
        add_help=False,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "-h", "--help",
        action="help",
        default=argparse.SUPPRESS,
        help="Show the 'devtools' usage guide."
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
        help="Subcommands"
    )

    # Register the HTTP status code explainer subcommand
    http_status.register(subparsers)

    # Register the text statistics subcommand
    text_stats.register(subparsers)

    # Register the color converter subcommand
    color_converter.register(subparsers)

    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main(["color_converter", "--hsvToRgb", "hsv(97, 63, 45)"])
