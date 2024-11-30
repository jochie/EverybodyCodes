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
        description='This program is used for one of the EverybodyCodes 2024 puzzles; Day 7, part 1'
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


def run_races(opts, data):
    results = []
    for key, oper in data:
        if opts.debug:
            print(f"{key} -> {oper}")
        sum = 0
        value = 10
        for ix in range(10):
            op = oper[ix % len(oper)]
            if op == "+":
                value += 1
            elif op == "=":
                pass
            elif op == "-":
                value -= 1
            else:
                print("oops?")
                sys.exit(1)
            sum += value
        if opts.debug:
            print(f"{key} -> {sum}")
        results.append([ key, sum ])
    return results

def main():
    """
    Main section, where we parse the command line options, read the
    stdin content, and act on it
    """
    data = []
    opts = parse_options()
    for line in sys.stdin:
        line = line.rstrip()
        if opts.debug:
            print("DEBUG: Line received: '{}'".format(line))
        line_match = re.match(r"([A-Z]+):(.*)", line)
        if line_match:
            data.append([line_match.group(1), line_match.group(2).split(",")])
        else:
            print(f"Malformed line? {line}")
            sys.exit(1)
    # Done parsing and pre-processing input

    results = run_races(opts, data)
    results.sort(key=lambda x: x[1], reverse=True)
    keys = [entry[0] for entry in results]
    print(f"Outcome: {''.join(keys)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
