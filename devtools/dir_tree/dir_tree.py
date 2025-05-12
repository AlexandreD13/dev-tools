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

DIRECTORY: str = os.getcwd().split("\\")[-1]
FOLDER_COLOR: str = f"{Fore.BLUE}{Style.BRIGHT}"
FILE_COLOR: str = f"{Fore.WHITE}{Style.BRIGHT}"
HIERARCHY_COLOR: str = f"{Fore.WHITE}{Style.DIM}"
NB_SPACES: int = 2


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

    parser.add_argument(
        "-d", "--depth",
        type=int,
        default=None,
        help="Limit the depth of the tree."
    )

    parser.set_defaults(func=run)


def run(args: argparse.Namespace) -> None:
    print(f"\n{FOLDER_COLOR}{DIRECTORY}/{Style.RESET_ALL}")

    paths = walk_directory(max_depth=args.depth)
    trimmed = trim_paths(paths)
    tree = build_tree(trimmed)

    print_tree(tree, depth=args.depth)


def walk_directory(max_depth=None):
    all_paths = []
    cwd = os.getcwd()

    for root, dirs, files in os.walk(cwd):
        rel = os.path.relpath(root, cwd)
        depth = 0 if rel == "." else rel.count(os.sep) + 1

        for d in dirs:
            all_paths.append(os.path.join(root, d))

        if max_depth is not None and depth >= max_depth:
            dirs[:] = []

        for f in files:
            all_paths.append(os.path.join(root, f))

    return all_paths


def trim_paths(all_paths):
    cwd = os.getcwd()
    base_parts = cwd.split(os.sep)[-2:]
    base = os.sep.join(base_parts)

    return [path.split(base)[-1].lstrip(os.sep).split(os.sep)
            for path in all_paths]


def build_tree(paths):
    tree = {}
    for parts in paths:
        node = tree
        for part in parts:
            node = node.setdefault(part, {})

    return tree


def is_avoided(name):
    return any(avoid in name for avoid in AVOIDED_FOLDER)


def sort_entries(node):
    return sorted(
        node.items(),
        key=lambda item: (not bool(item[1]), item[0])
    )


def make_connector(is_last: bool) -> str:
    return f"{HIERARCHY_COLOR}{'└──' if is_last else '├──'}{Style.RESET_ALL} "


def make_next_prefix(prefix: str, is_last: bool) -> str:
    if is_last:
        return prefix + " " * NB_SPACES

    return prefix + f"{HIERARCHY_COLOR}│{' ' * NB_SPACES}{Style.RESET_ALL}"


def print_file(name: str, branch: str) -> None:
    print(f"{branch}{FILE_COLOR}{name}{Style.RESET_ALL}")


def print_folder(name, children, branch, depth, level, prefix, is_last):
    label = f"{name}/"
    colored_label = f"{FOLDER_COLOR}{label}{Style.RESET_ALL}"

    if is_avoided(name):
        print(f"{branch}{colored_label}{Fore.RED}...{Style.RESET_ALL}")
        return

    if depth is not None and (level + 1) >= depth:
        print(f"{branch}{colored_label}{Fore.RED}...{Style.RESET_ALL}")
        return

    print(f"{branch}{colored_label}")
    next_prefix = make_next_prefix(prefix, is_last)
    print_tree(children, prefix=next_prefix, depth=depth, level=level + 1)


def print_tree(node, prefix="", depth=None, level=0):
    if depth is not None and level >= depth:
        return

    entries = sort_entries(node)

    for idx, (name, children) in enumerate(entries):
        is_last = idx == len(entries) - 1
        connector = make_connector(is_last)
        branch = prefix + connector
        if children:
            print_folder(name, children, branch, depth, level, prefix, is_last)
        else:
            print_file(name, branch)
