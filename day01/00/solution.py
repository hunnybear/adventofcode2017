#!/usr/bin/env python

import sys

def run(in_val):
    digits = [int(i) for i in in_val.strip()]

    sum_val = 0

    for idx in range(len(digits)):
        if digits[idx] == digits[idx-1]:
            sum_val += digits[idx]
    return sum_val


if __name__ == '__main__':
    in_val = sys.argv[1]
    print(run(in_val))
