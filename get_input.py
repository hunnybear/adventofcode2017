#!/usr/bin/env python

import os
import os.path
import urllib

_INPUT_FILENAME = 'input'


def _get_and_create_input_local_path(working_dir, day):

    day_str = str(day).zfill(2)

    day_path = os.path.join(working_dir, "day{0}".format(day_str))

    if not os.path.exists(day_path):
        os.mkdir(day_path)
    else:
        assert os.path.isdir(day_path)

    return os.path.join(day_path, _INPUT_FILENAME)


def run(working_dir):

    day = 1

    while True:
        input_url = "http://adventofcode.com/2017/day/{0}/input".format(str(day))
        input_local_path = _get_and_create_input_local_path(working_dir, day)

        urllib.urlretrieve(input_url, input_local_path)

        day += 1


if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    run(this_dir)
