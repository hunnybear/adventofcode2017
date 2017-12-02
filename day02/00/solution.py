#!/usr/bin/env python

"""
Solution for first problem on day 2.
"""

import sys

_TEST_VAL = """5 1 9 5
7 5 3
2 4 6 8"""


def test():
    """
    Test my solution using the test case provided by AOC.
    """
    assert run(_TEST_VAL) == 18


def run(input_val):
    """
    Main function for the solution.
    """

    checksum = 0
    for row in input_val.splitlines():
        row_vals = [int(v) for v in row.split()]

        diff = max(row_vals) - min(row_vals)
        checksum += diff

    return checksum


if __name__ == '__main__':
    in_val = sys.argv[1]

    print(run(in_val))
