from colorama import Fore, Style

import argparse
import random


LOREM_WORDS = (
    "lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt "
    "ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco "
    "laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in "
    "voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat "
    "non proident sunt in culpa qui officia deserunt mollit anim id est laborum"
).split()


def register(subparsers):
    parser = subparsers.add_parser(
        "lorem_ipsum",
        help="Generate lorem ipsum text.",
        add_help=False,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "-h", "--help",
        action="help",
        default=argparse.SUPPRESS,
        help="Show the 'lorem_ipsum' tool usage guide."
    )

    parser.add_argument(
        "--paragraphs", "-p",
        type=int, default=3,
        metavar="N", help="Number of paragraphs to generate.")

    parser.add_argument(
        "--sentences", "-s",
        type=int, default=10,
        metavar="N", help="Number of sentences/paragraphs to generate.")

    parser.set_defaults(func=run)


def run(args):
    text = lorem_ipsum(paragraphs=args.paragraphs, sentences=args.sentences)

    print(f"{Fore.BLUE}{Style.BRIGHT}" + text + f"{Style.RESET_ALL}")


def lorem_ipsum(paragraphs, sentences) -> str:
    return "\n\n".join(
        generate_paragraph(sentences)
        for _ in range(paragraphs)
    )


def generate_paragraph(sentence_count) -> str:
    return " ".join(generate_sentence() for _ in range(sentence_count))


def generate_sentence() -> str:
    length = random.randint(8, 15)
    words = random.choices(LOREM_WORDS, k=length)
    sentence = " ".join(words).capitalize() + "."

    return sentence
