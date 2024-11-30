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
        description='This program is used for one of the EverybodyCodes 2024 puzzles; Day 8, part 3'
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
        priests  =   2
        acolytes =   5
        blocks   = 300
    else:
        # The Real Deal
        priests  =    914567
        acolytes =        10
        blocks   = 202400000

    columns = []
    # Done
    if opts.verbose:
        print(f"Blocks to play with: {blocks}")
    width = 1
    total = 0
    thickness = 1

    while True:
        columns.append(0)
        for ix in range(len(columns)):
            columns[ix] += thickness
        total += width * thickness
        if opts.verbose:
            print(f"Width: {width}; Blocks used: {total}; Thickness was {thickness}")
            print(f"Columns: {columns}")
        if total >= blocks:
            print(f"Width is {width}, extra blocks needed: {total - blocks}")
            if opts.debug:
                print(f"Columns: {columns}")

            # First (middle) column only counts for 1
            multiplier = 1
            removed = 0
            for ix in range(len(columns) - 1):
                empty = (priests * width * columns[ix]) % acolytes
                if opts.verbose:
                    print(f"Column {ix + 1} (height {columns[ix]}: Leave {empty} blocks empty?")
                removed += empty * multiplier

                # All the other columns count for 2
                multiplier = 2
            print(f"Blocks to leave empty: {removed}")
            print(f"To buy extra: {total - blocks - removed}")
            break
        width += 2
        thickness = (thickness * priests) % acolytes + acolytes
    return 0

if __name__ == "__main__":
    sys.exit(main())
