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
        description='This program is used for one of the EverybodyCodes 2024 puzzles; Day 5, part 1'
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


def process_round(opts, iteration, columns):
    # Select the clapper for this round
    col = (iteration - 1) % len(columns)

    clapper =  columns[col][0]
    if opts.debug:
        print(f"Selected clapper: {clapper} from column {col + 1}")
    columns[col] = columns[col][1:]
    if opts.debug:
        print(columns)

    dir_down = True
    hi5_column = (col + 1) % len(columns)
    if opts.debug:
        print(f"Walking down column {hi5_column + 1}")

    if clapper <= len(columns[hi5_column]):
        # Insert at position <clapper> (1-index based)
        columns[hi5_column] = columns[hi5_column][:clapper-1] + [ clapper ] + columns[hi5_column][clapper-1:]
    elif clapper <= 2 * len(columns[hi5_column]):
        offset = len(columns[hi5_column]) - (clapper - len(columns[hi5_column]))
        # Insert at position <clapper> - <column length>
        columns[hi5_column] = columns[hi5_column][:offset + 1] + [ clapper ] + columns[hi5_column][offset + 1:]
    else:
        print("Uh oh")
        sys.exit(1)
    return


def main():
    """
    Main section, where we parse the command line options, read the
    stdin content, and act on it
    """
    columns = None
    opts = parse_options()
    for line in sys.stdin:
        line = line.rstrip()
        if opts.debug:
            print("DEBUG: Line received: '{}'".format(line))

        # Transpose the numbers
        numbers = line.split(" ")
        if columns is None:
            columns = []
            for i in range(len(numbers)):
                columns.append([])

        for ix, col in enumerate(numbers):
            columns[ix].append(int(col))

    # Done parsing and pre-processing input
    if opts.debug:
        print(columns)

    iteration = 1
    while True:
        process_round(opts, iteration, columns)
        if opts.debug:
            print(columns)
        number = "".join([ str(column[0]) for column in columns ])
        print(f"Number for round {iteration}: {number}")
        print()
        if iteration == 10:
            break
        iteration += 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
