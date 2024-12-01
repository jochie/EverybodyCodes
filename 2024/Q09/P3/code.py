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
        description='This program is used for one of the EverybodyCodes 2024 puzzles; Day 9, part 3'
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


STAMPS = [101, 100, 75, 74, 50, 49, 38, 37, 30, 25, 24, 20, 16, 15, 10, 5, 3, 1]
         
# The naive approach (compared to what follows in P2)
def naive_stamp_beetles(opts, brightness):
    count = 0
    while brightness > 0:
        for stamp in STAMPS:
            if brightness >= stamp:
                count += 1
                brightness -= stamp
                break
    return count

brightness_cache = {}

def stamp_beetles(opts, brightness):
    if brightness in brightness_cache:
        # Minor optimization
        if opts.debug:
            print(f"Using cached value for {brightness}: {brightness_cache[brightness]}")
        return brightness_cache[brightness]

    upper_limit = naive_stamp_beetles(opts, brightness)
    if opts.verbose:
        print(f"The naive approach gives us {upper_limit} as an upper limit, for {brightness}.")
    attempts = []
    for stamp in STAMPS:
        attempts.append([stamp, [stamp]])
    round = 0
    while True:
        round += 1
        if opts.debug:
            print(f"Round {round} - Checking {len(attempts)} attempts:")
        new_attempts = []

        for total, collected in attempts:
            last = collected[-1]
            if opts.debug:
                print(f"{total} -> {collected} - {last}")

            for stamp in STAMPS:
                if stamp > last:
                    # Skip the stamps that are too big
                    continue

                if total + stamp > brightness:
                    # Skip, too big
                    continue

                if total + stamp == brightness:
                    # Found it!
                    brightness_cache[brightness] = len(collected) + 1
                    if opts.verbose:
                        # print(f"Found solution for {brightness}: {collected + [stamp]}")
                        print(f"Found solution for {brightness}: {len(collected) + 1}")
                    return len(collected) + 1

                if total + stamp * (upper_limit - len(collected)) < brightness:
                    # Unreachable solution
                    continue
                new_attempts.append([total + stamp, collected + [stamp]])

        attempts = new_attempts


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
        min_count = None

        # Round up, when sparkball is an odd number
        spark_base = int((sparkball - 100) / 2 + 0.5)

        # No point in checking all 100 combinations, since that should
        # just be the reverse combinations of the earlier ones
        for offset in range(51):
            spark_1 = spark_base + offset
            spark_2 = sparkball - spark_1
            count1 = stamp_beetles(opts, spark_1)
            count2 = stamp_beetles(opts, spark_2)
            if opts.debug:
                print(f"Comparing solutions for {spark_1} and {spark_2}, offset = {abs(spark_1 - spark_2)} => {count1} and {count2}")
            if not min_count or count1 + count2 < min_count[0] + min_count[1]:
                min_bright = [spark_1, spark_2]
                min_count = [count1, count2]
                if opts.verbose:
                    print(f"Setting a new set of minimum values: {min_bright}; {min_count}")

        if opts.verbose:
            print(f"Sparkball {sparkball} -> {min_count[0]} + {min_count[1]} = {min_count[0] + min_count[1]} beetles (for brightness {min_bright[0]} and {min_bright[1]}).")
        total += min_count[0] + min_count[1]

    print(f"Total: {total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
