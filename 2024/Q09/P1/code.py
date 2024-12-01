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
        description='This program is used for one of the EverybodyCodes 2024 puzzles; Day 9, part 1'
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


# 4 available stamps
# - 1
# - 3
# - 5
# - 10

# The naive approach (compared to what follows in P2)
def stamp_beetles(opts, brightness):
    beetles = [10, 5, 3, 1]
    count = 0
    while brightness > 0:
        for beetle in beetles:
            if brightness >= beetle:
                count += 1
                brightness -= beetle
                break
    return count


def main():
    """
    Main section, where we parse the command line options, read the
    stdin content, and act on it
    """
    sb_list = []
    opts = parse_options()
    for line in sys.stdin:
        sparkballs = int(line.rstrip())
        sb_list.append(sparkballs)
        if opts.debug:
            print("DEBUG: Line received: '{}'".format(line))
    # Done

    total = 0
    if opts.debug:
        print(sb_list)
    for sparkball in sb_list:
        count = stamp_beetles(opts, sparkball)
        if opts.verbose:
            print(f"Sparkball {sparkball} -> {count} beetles.")
        total += count

    print(f"Total: {total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
