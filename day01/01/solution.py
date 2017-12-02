#!/usr/bin/env python

"""
--- Part Two ---

You notice a progress bar that jumps to 50% completion. Apparently, the door
isn't yet satisfied, but it did emit a star as encouragement. The
instructions change:

Now, instead of considering the next digit, it wants you to consider the digit
halfway around the circular list. That is, if your list contains 10 items,
only include a digit in your sum if the digit 10/2 = 5 steps forward matches
it. Fortunately, your list has an even number of elements.

For example:

1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
1221 produces 0, because every comparison is between a 1 and a 2.
123425 produces 4, because both 2s match each other, but no other digit has a match.
123123 produces 12.
12131415 produces 4.
"""

import sys

def test():
    assert run('1212') == 6
    assert run('1221') == 0
    assert run('123425') == 4
    assert run('123123') == 12
    assert run('12131415') == 4

def run(in_val):
    digits = [int(i) for i in in_val.strip()]

    sum_val = 0

    for idx in range(len(digits)):
        if digits[idx] == digits[idx-(len(in_val)/2)]:
            sum_val += digits[idx]
    return sum_val


if __name__ == '__main__':
    in_val = sys.argv[1]
    print(run(in_val))
