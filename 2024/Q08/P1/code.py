#!/usr/bin/env python3

"""
Python code template for EverybodyCodes programs
"""

import argparse
import sys

def parse_options():
    """
    Parser command line options
    """
    parser = argparse.ArgumentParser(
        description='This program is used for one of the EverybodyCodes 2024 puzzles; Day 8, part 1'
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

def main():
    """
    Main section, where we parse the command line options, read the
    stdin content, and act on it
    """
    opts = parse_options()
    for line in sys.stdin:
        blocks = int(line.rstrip())
        if opts.debug:
            print("DEBUG: Line received: '{}'".format(line))
    # Done
    if opts.verbose:
        print(f"Blocks to play with: {blocks}")

    width = 1
    total = 0

    while True:
        total += width
        if opts.verbose:
            print(f"Width: {width}; Blocks used: {total}")
        if total >= blocks:
            print(f"Width is {width}, extra blocks needed: {total - blocks}")
            print(f"Multiply those two: {width * (total - blocks)}")
            break
        width += 2

    return 0

if __name__ == "__main__":
    sys.exit(main())
