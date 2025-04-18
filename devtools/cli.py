from colorama import init

from devtools.color_converter import color_converter
from devtools.dir_tree import dir_tree
from devtools.http_status import http_status
from devtools.lorem_ipsum import lorem_ipsum
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

    color_converter.register(subparsers)    # Register the Color converter subcommand
    http_status.register(subparsers)        # Register the HTTP status code explainer subcommand
    lorem_ipsum.register(subparsers)        # Register the Lorem ipsum text generator subcommand
    text_stats.register(subparsers)         # Register the Text statistics subcommand
    dir_tree.register(subparsers)           # Register the Directory Tree subcommand

    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main(["dir_tree"])
