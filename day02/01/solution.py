#!/usr/bin/env python

"""
Solution script for the second day 2 problem.
"""

import sys

_TEST_VAL = """5 9 2 8
9 4 7 3
3 8 6 5"""


def test():
    assert run(_TEST_VAL) == 9


def run(input_val):
    """
    Main body for solution
    """

    checksum = 0
    for row in input_val.splitlines():
        # Sort the rows, so we can save loops.
        row_vals = sorted([int(v) for v in row.split()], reverse=True)

        while row_vals:
            a = row_vals.pop(0)
            for b in row_vals:
                if not a % b:
                    break
            else:
                # If we haven't found an even division, move to the
                # next numerator.
                continue

            checksum += a / b
            break

    return checksum


if __name__ == '__main__':
    in_val = sys.argv[1]

    print(run(in_val))
