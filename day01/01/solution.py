#!/usr/bin/env python

"""
Solution script for the secont problem on day 1 of AOC.
"""

import sys


def test():
    """
    Test my solution with examples from the AOC problem description.
    """

    assert run('1212') == 6
    assert run('1221') == 0
    assert run('123425') == 4
    assert run('123123') == 12
    assert run('12131415') == 4


def run(in_val):
    digits = [int(i) for i in in_val.strip()]

    sum_val = 0

    for idx in range(len(digits)):
        if digits[idx] == digits[idx - (len(in_val) / 2)]:
            sum_val += digits[idx]
    return sum_val


if __name__ == '__main__':
    in_val = sys.argv[1]
    print(run(in_val))
