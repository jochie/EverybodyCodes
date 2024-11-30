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
        description='This program is used for one of the EverybodyCodes 2024 puzzles; Day 7, part 2'
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

    parser.add_argument('-t', '--track',
                        help="The file with track information",
                        required=True)

    return parser.parse_args()


def read_track_data(track):
    left, right, top, bottom = "", "", "", ""
    with open(track, "r", encoding="utf-8") as track_file:
        lines = []
        for line in track_file.readlines():
            lines.append(line.strip())
        top = lines[0][1:]
        left = lines[0][0:1]
        bottom = lines[len(lines) - 1][::-1]

        for ix in range(len(lines) - 2):
            left = lines[ix + 1][0:1] + left
            right = right + lines[ix + 1][-1:]
    result = top + right + bottom + left
    return result

def run_races(opts, data, track_data):
    results = []
    if opts.debug:
        print(f"Track length: {len(track_data)}; data length: {len(data[0][1])}")
    # Need to account for the case where the length of the list of
    # operators does not divide cleanly into the length of the track,
    # which causes the pairs to line up differently each time.
    for key, oper in data:
        sum = 0
        value = 10
        data_ix = 0
        for loop in range(10):
            if opts.debug:
                print(f"Loop {loop + 1}\n")
                print(f"{key} -> {oper}")
            for ix in range(len(track_data)):
                op = track_data[ix]
                if op in ['=', 'S']:
                    op = oper[data_ix % len(oper)]
                data_ix += 1
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
    if opts.debug:
        print(f"RESULTS: {results}")
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
    track_data = read_track_data(opts.track)
    results = run_races(opts, data, track_data)
    results.sort(key=lambda x: x[1], reverse=True)
    keys = [entry[0] for entry in results]
    print(f"Outcome: {''.join(keys)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
