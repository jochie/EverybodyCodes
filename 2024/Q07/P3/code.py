#!/usr/bin/env python3

"""
Python code template for EverybodyCodes programs
"""

# Surely this can be optimized somehow, but I'm not immediately seeing
# it. Perhaps by running all 9240 plans along with the opponent's, but
# that will still "only" cut the time in half, and I think this needs
# a more significant improvement.

import argparse
import re
import sys

def parse_options():
    """
    Parser command line options
    """
    parser = argparse.ArgumentParser(
        description='This program is used for one of the EverybodyCodes 2024 puzzles; Day 7, part 3'
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


def read_track_data(opts):
    with open(opts.track, "r", encoding="utf-8") as track_file:
        lines = []
        for line in track_file.readlines():
            lines.append(line.strip())

        # Erase the 'S'
        lines[0] = ' ' + lines[0][1:]
        # Start following the track at (0,1)
        row = 0
        col = 1
        result = ''
        while True:
            result += lines[row][col]
            if opts.debug:
                print(f"RESULT: {result}")
            lines[row] = lines[row][:col] + ' ' + lines[row][col+1:]
            if row > 0 and col < len(lines[row - 1]) and lines[row - 1][col] != ' ':
                row -= 1
            elif col < len(lines[row]) - 1 and lines[row][col + 1] != ' ':
                col += 1
            elif row < len(lines) - 1 and col < len(lines[row + 1]) and lines[row + 1][col] != ' ':
                row += 1
            elif col > 0 and lines[row][col - 1] != ' ':
                col -= 1
            else:
                if opts.debug:
                    print("Done?")
                result += "S"
                break

    return result


def rec_generate_plans(opts, prefix, opers, plan_list):
    if len(prefix) == 11:
        plan_list.append(prefix)
        return
    for oper, left in opers.items():
        if left == 0:
            # SKip
            continue
        opers[oper] -= 1
        rec_generate_plans(opts, prefix + oper, opers, plan_list)
        opers[oper] += 1


# Generate all 11! / (5! 3! 3!) = 9240 possible plans
def generate_plans(opts):
    plan_list = []
    rec_generate_plans(opts, '', {'+': 5, '-': 3, '=': 3}, plan_list)

    if opts.debug:
        print(f"Plans generated: {len(plan_list)}")
        print(plan_list)
    return plan_list


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

        for loop in range(2024):
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
    track_data = read_track_data(opts)

    wins = 0
    losses = 0
    for ix, plan in enumerate(generate_plans(opts)):
        combination = [
            [ "T", data[0][1] ],
            [ "U", list(plan) ]
        ]
        results = run_races(opts, combination, track_data)
        results.sort(key=lambda x: x[1], reverse=True)
        keys = [entry[0] for entry in results]
        if opts.verbose:
            print(f"{ix} - Outcome: {''.join(keys)}")
        if keys[0] == 'U':
            wins += 1
        else:
            losses += 1
        if opts.verbose:
            print(f"{ix} - Plan {plan} - Wins/losses: {wins}/{losses}")

    print(f"Wins/losses: {wins}/{losses}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
