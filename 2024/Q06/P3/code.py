#!/usr/bin/env python3

"""
Python code template for EverybodyCodes programs
"""

import argparse
import re
import sys

def parse_options():
    """
    Parser command line options
    """
    parser = argparse.ArgumentParser(
        description='This program is used for one of the EverybodyCodes 2024 puzzles; Day 6, part 3'
    )
    parser.add_argument('-d', '--debug',
                        help="Enable debug output",
                        default=False,
                        action='store_true')
    parser.add_argument('-n', '--dryrun',
                        help="Enable dryrun (noop) output",
                        default=False,
                        action='store_true')
    parser.add_argument('-v', '--verbose',
                        help="Enable verbose output",
                        default=False,
                        action='store_true')
    return parser.parse_args()


# "... the potency of each apple depends on whether it shares
# resources with other apples."
#
# The most powerful one is the apple that, in our example and actual
# challenge, has no other apples at the same depth, apparently.
#
# This solution assumes all nodes (except RR) have the same length of
# name, otherwise we will need to track the depth separately.

def find_apple_paths(opts, tree, path, node, paths):
    if opts.debug:
        print(f"Checking paths at {path}{node}")

    if node not in tree:
        # Nothing to do here
        return None

    for dest in tree[node]:
        if dest in ['BUG', 'ANT']:
            # Ignore these pests
            continue
        if opts.debug:
            print(f"Checking paths at {path}{node}{dest}")
        if dest == "@":
            next_path = path + node + "@"
            if len(next_path) not in paths:
                paths[len(next_path)] = []
            paths[len(next_path)].append(next_path)
        else:
            find_apple_paths(opts, tree, path + node, dest, paths)
    return


def print_tree(opts, tree, prefix, node):
    print(f"{prefix}{node}:")
    if node in tree:
        for dest in tree[node]:
            if dest in ['BUG', 'ANT']:
                # Ignore these pests
                continue
            print_tree(opts, tree, prefix + "    ", dest)
    return

def main():
    """
    Main section, where we parse the command line options, read the
    stdin content, and act on it
    """
    opts = parse_options()
    tree = {}
    for line in sys.stdin:
        line = line.rstrip()
        if opts.debug:
            print("DEBUG: Line received: '{}'".format(line))
        node = re.match(r"([A-Z]+):(.*)", line)
        if node:
            tree[node.group(1)] = node.group(2).split(",")
        else:
            print(f"Malformed line? {line}")
            sys.exit(1)
    # Done parsing and pre-processing input
    if opts.debug:
        print_tree(opts, tree, '', 'RR')

    paths = {}
    find_apple_paths(opts, tree, "", "RR", paths)
    for path_len, path_list in paths.items():
        if len(path_list) == 1:
            print(f"Found one that doesn't share: {path_list[0]}")
            # Now the first of every 4 letters, 'RR' is the exception.
            letters = "R"
            offset = 2
            while offset < len(path_list[0]):
                letters += path_list[0][offset]
                offset += 4
            print(f"Shortened form: {letters}")
            break

    return 0


if __name__ == "__main__":
    sys.exit(main())
