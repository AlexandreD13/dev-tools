from collections import Counter, OrderedDict
from colorama import Fore, Style

import argparse
import json
import os
import re

results = {}


def register(subparsers):
    parser = subparsers.add_parser(
        "text_stats",
        help="Generates statistics on a text.",
        add_help=False,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "-h", "--help",
        action="help",
        default=argparse.SUPPRESS,
        help="Show the 'text_stats' tool usage guide."
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", type=str, help="Path to file.")
    group.add_argument("--string", type=str, help="String of text.")

    parser.set_defaults(func=run)


def run(args):
    if args.file:
        if not args.file.endswith(".txt"):
            print(f"\n{Fore.RED}{Style.DIM}Error: Only '.txt' files are allowed.{Style.RESET_ALL}")
            return
        if not os.path.isfile(args.file):
            print(f"\n{Fore.RED}{Style.DIM}Error: File '{args.file}' does not exist.{Style.RESET_ALL}")
            return

        with open(args.file, "r", encoding="utf-8") as f:
            text = f.read()

        word_list = get_word_list(text)
        character_string = get_character_string(text)

        results["Number of words"] = len(word_list)
        results["Number of characters"] = len(character_string)
        results["Number of lines"] = len(text.splitlines())
        results["Number of unique words"] = len(set(word_list))
        results["Most common words"] = Counter([word for word in word_list if len(word) > 2]).most_common(5)
        results["Character frequencies"] = OrderedDict(
            sorted(dict(Counter(re.sub(r'\d', '', character_string.lower()))).items())
        )

        print(f"\n{Fore.BLUE}{Style.BRIGHT}" + json.dumps(results, ensure_ascii=False, indent=4) + f"{Style.RESET_ALL}")

    if args.string:
        print("string")


def get_word_list(text):
    text = re.sub(r"[.,!?()]", " ", text)
    text = text.split()

    return text


def get_character_string(text):
    text = re.sub(r"[.,!? \n'()-]", "", text)

    return text
