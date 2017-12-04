#!/usr/bin/env python

"""
Run aoc solutions. Yes, I'm this lazy. and this flight is long, and I'm bored.

Appropriate responses to this include "why do this hunnybear?" and "What made
you this way?"

Am I killing flies with a howitzer? no, I'm klling them with nukes. Could I
just make sure I name my folders consistently instead of doing this silly
coercing folder names to integers and sorting off of that? sure, but, I remind
you that I'm bored on this flight. Is anyone going to read this other than me
and maybe Alex (Hi alex!). unlikely.

Anyway. You've been warned.

"""

import argparse
import glob
import os
import os.path
import re
import sys

_DAY_RE_STR = '^day(\d+)$'
_SOLUTION_FILENAME = 'solution.py'
_INPUT_FILENAME = 'input'

_USAGE = """runner.py [day problem]
    Either run runner.py with no arguments to run the most recent solution, or
    run it with two arguments (day, problem) to run a specific day and problem."""


def _parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('day', type=int, default=None, nargs='?')
    parser.add_argument('problem', type=int, default=None, nargs='?')
    parser.add_argument('--test', '-t', action='store_true')

    args = parser.parse_args()

    return args


def _get_day_dir(main_dir, problem_day):
    problem_day = int(problem_day)
    day_dir_name = None
    for name in os.listdir(main_dir):
        path = os.path.join(main_dir, name)
        if not os.path.isdir(path):
            continue

        match = re.match(_DAY_RE_STR, name)
        if not match:
            continue

        dir_int = int(match.groups()[0])
        if dir_int == problem_day:
            if day_dir_name is not None:
                msg = "Duplicate directories found for day {0}!:".format(dir_int)
                msg += '\n\t{0}'.format(','.join([day_dir_name, name]))
                raise EnvironmentError(msg)
            day_dir_name = name

    if day_dir_name is not None:
        return os.path.join(main_dir, day_dir_name)
    return None


def _get_problem_dir(main_dir, problem_day, problem_number):

    day_dir = _get_day_dir(main_dir, problem_day)
    if day_dir is None:
        return None

    problem_number = int(problem_number)

    dir_name = None

    for name in os.listdir(day_dir):
        path = os.path.join(day_dir, name)
        if not os.path.isdir(path):
            continue
        if not name.isdigit():
            continue
        if int(name) == problem_number:
            if dir_name is not None:
                msg = "Duplicate problems found for problem {0} in day {1}"
                raise EnvironmentError(msg.format(problem_number, problem_day))

            dir_name = name

    if dir_name is not None:
        return os.path.join(day_dir, dir_name)
    return None


def get_input_for_problem(problem_dir):

    input_path = os.path.join(problem_dir, _INPUT_FILENAME)
    if os.path.isfile(input_path):
        with open(input_path, 'r') as fh:
            return fh.read(input_path)

    else:
        day_dir = os.path.dirname(problem_dir)
        input_path = os.path.join(day_dir, _INPUT_FILENAME)
        if os.path.isfile(input_path):
            with open(input_path, 'r') as fh:
                return fh.read()
    raise EnvironmentError('Could not find input file!')



def run_solution(main_dir, day=None, problem=None, test=False):
    if day is not None:
        day = int(day)
    if problem is not None:
        problem = int(problem)

    solutions_glob = os.path.join(main_dir, '*', '*', _SOLUTION_FILENAME)
    solution_paths = glob.glob(solutions_glob)

    solutions = {}

    for path in solution_paths:
        re_str = '^{0}/day(\d+)/(\d+)/{1}$'.format(main_dir, _SOLUTION_FILENAME)

        match = re.match(re_str, path)
        if match is None:
            continue

        glob_day, glob_problem = tuple(int(val) for val in match.groups())
        if day is not None and day != glob_day:
            continue

        if problem is not None and problem != glob_problem:
            continue

        solutions_key = (glob_day, glob_problem)
        if solutions_key in solutions:
            # TODO better messaging
            raise EnvironmentError('duplicate day/problem found!')

        solutions[solutions_key] = path
    solution_path = solutions[max(solutions)]
    return _run_exact_solution(os.path.dirname(solution_path), test=test)


def _run_exact_solution(solution_dir, test=False):
    """
    Run the solution in the exact specified directory
    """

    sys.path.append(solution_dir)
    import solution

    if test:
        try:
            solution.run
        except AttributeError:
            solution_filepath = os.path.join(solution_dir, _SOLUTION_FILENAME)
            "The problem solution {0} does not contain a run() function!"
            raise EnvironmentError(msg.format(solution_filepath))

        solution.test()

        # if we hit this, no exceptions, so success
        return "Success!"
    else:
        input_val = get_input_for_problem(solution_dir)
        return solution.run(input_val)





def run():

    args = _parse_args()

    problem = args.problem
    day = args.day
    test = args.test

    this_dir = os.path.dirname(__file__)
    try:
        res = run_solution(this_dir, day=day, problem=problem, test=test)

    except EnvironmentError as exc:
        sys.exit(repr(exc))

    print(res)


if __name__ == '__main__':
    run()
