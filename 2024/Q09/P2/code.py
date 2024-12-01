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
        description='This program is used for one of the EverybodyCodes 2024 puzzles; Day 9, part 2'
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


# Available stamps
# -  1
# -  3
# -  5
# - 10
# - 15
# - 16
# - 20
# - 24
# - 25
# - 30

STAMPS = [30, 25, 24, 20, 16, 15, 10, 5, 3, 1]

best_count = None

def rec_stamp_beetles(opts, brightness, upper, stamped):
    global best_count

    if opts.debug:
        print(f"best_count: {len(best_count) if best_count else 'N/A'} - {brightness}; {upper}; {len(stamped)}")
    if best_count and brightness > 0 and len(stamped) >= len(best_count):
        # No point, already exceeding the best solution so far.
        if opts.debug:
            print(f"Aborting after {len(stamped)} and {brightness} left.")
        return
    if best_count and brightness > (len(best_count) - len(stamped)) * upper:
        if opts.debug:
            print(f"Aborting because unreachable with {len(best_count) - len(stamped)} x {upper}")
        return

    if brightness == 0:
        if opts.debug:
            print(f"New best: {len(stamped)} -> {stamped}")
        best_count = stamped
        return

    for stamp in STAMPS:
        if stamp > upper:
            continue

        if brightness >= stamp:
            rec_stamp_beetles(opts, brightness - stamp, stamp, stamped + [ stamp ])
    # Done


def stamp_beetles(opts, brightness):
    global best_count

    best_count = None

    rec_stamp_beetles(opts, brightness, STAMPS[0],  [])
    if opts.debug:
        print(f"Collected stamps: {best_count}")
    return len(best_count)


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
