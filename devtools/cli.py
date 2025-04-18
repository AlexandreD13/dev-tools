from colorama import init
from devtools.color_converter import color_converter
from devtools.http_status import http_status
from devtools.text_stats import text_stats

import argparse


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

    http_status.register(subparsers)        # Register the HTTP status code explainer subcommand
    text_stats.register(subparsers)         # Register the text statistics subcommand
    color_converter.register(subparsers)    # Register the color converter subcommand

    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main(["color_converter", "--rgbToHsv", "rgb(0, 118, 132)"])
