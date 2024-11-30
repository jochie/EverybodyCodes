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
        description='This program is used for one of the EverybodyCodes 2024 puzzles; Day 8, part 2'
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

    if False:
        # Sample
        priests  =  3
        acolytes =  5
        blocks   = 50
    else:
        # The Real Deal
        priests  =      992
        acolytes =     1111
        blocks   = 20240000

    # Done
    if opts.verbose:
        print(f"Blocks to play with: {blocks}")
    width = 1
    total = 0
    thickness = 1

    while True:
        total += width * thickness
        if opts.verbose:
            print(f"Width: {width}; Blocks used: {total}")
        if total >= blocks:
            print(f"Width is {width}, extra blocks needed: {total - blocks}")
            print(f"Multiply those two: {width * (total - blocks)}")
            break
        width += 2
        thickness = (thickness * priests) % acolytes
    return 0

if __name__ == "__main__":
    sys.exit(main())
