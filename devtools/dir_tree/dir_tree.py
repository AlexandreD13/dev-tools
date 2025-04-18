from colorama import Fore, Style

import argparse
import os


AVOIDED_FOLDER: list = [
    "__pycache__",
    "build",
    "dist",
    ".egg-info",
    ".git",
    ".idea",
    "venv",
    ".venv",
    "bin",
    "obj",
    "node_modules",
    "cmake-build-debug",
    "dependencies",
    ".vs",
    ".vscode",
    "out",
    "SVG_Icons",
    "test_cases",
    ".github",
    "Libraries",
    "third_party",
    "x64"
]

DIRECTORY       : str = os.getcwd().split("\\")[-1]

FOLDER_COLOR    : str = f"{Fore.BLUE}{Style.BRIGHT}"
FILE_COLOR      : str = f"{Fore.WHITE}{Style.BRIGHT}"
HIERARCHY_COLOR : str = f"{Fore.WHITE}{Style.DIM}"
NB_SPACES       : int = 2


# - tree
#   - Print a tree view of a directory (like tree command).
#   - Optional: limit depth, include hidden files.
def register(subparsers):
    parser = subparsers.add_parser(
        "dir_tree",
        help="Prints out the directory hierarchy.",
        add_help=False,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "-h", "--help",
        action="help",
        default=argparse.SUPPRESS,
        help="Show the 'dir_tree' tool usage guide."
    )

    parser.set_defaults(func=run)


def run(args):
    print(f"\n{FOLDER_COLOR}{DIRECTORY}/{Style.RESET_ALL}")

    paths = walk_directory()
    trimmed = trim_paths(paths)
    tree = build_tree(trimmed)

    print_tree(tree)


def walk_directory():
    all_paths = []
    for root, dirs, files in os.walk(os.getcwd()):
        for f in files:
            all_paths.append(os.path.join(root, f))

    return all_paths


def trim_paths(all_paths):
    cwd = os.getcwd()
    base_parts = cwd.split(os.sep)[-2:]
    base = os.sep.join(base_parts)

    trimmed = []
    for p in all_paths:
        rel = p.split(base)[-1].lstrip(os.sep)
        parts = rel.split(os.sep)
        trimmed.append(parts)

    return trimmed


def build_tree(paths):
    tree = {}
    for parts in paths:
        node = tree
        for part in parts:
            if part not in node:
                node[part] = {}

            node = node[part]

    return tree


def is_avoided(name):
    return any(av in name for av in AVOIDED_FOLDER)


def print_tree(node, prefix=""):
    folders = []
    files = []

    for name, children in node.items():
        if children:
            folders.append((name, children))
        else:
            files.append((name, children))

    entries = sorted(folders) + sorted(files)
    total = len(entries)

    for i, (name, children) in enumerate(entries):
        is_last = (i == total - 1)
        connector = f"{HIERARCHY_COLOR}{'└──' if is_last else '├──'}{Style.RESET_ALL} "

        new_prefix = prefix + (f"{Fore.WHITE}" + " " * NB_SPACES + f"{Style.RESET_ALL}" if is_last else f"{HIERARCHY_COLOR}│" + " " * NB_SPACES + f"{Style.RESET_ALL}")

        if children:
            color = FOLDER_COLOR
            label = f"{name}/{Fore.RED}...{Style.RESET_ALL}" if is_avoided(name) else f"{name}/{Style.RESET_ALL}"
            print(f"{prefix}{connector}{color}{label}")
            if not is_avoided(name):
                print_tree(children, new_prefix)
        else:
            print(f"{prefix}{connector}{FILE_COLOR}{name}{Style.RESET_ALL}")
