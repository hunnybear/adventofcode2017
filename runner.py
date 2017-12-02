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



def get_input_for_problem(main_dir, problem_day, problem_number):

    problem_dir = _get_problem_dir(main_dir, problem_day, problem_number)

    input_path = os.path.join(problem_dir, _INPUT_FILENAME)
    if os.path.isfile(input_path):
        with open(input_path, 'r') as fh:
            return fh.read(input_path)

    else:
        day_dir = _get_day_dir(main_dir, problem_day)
        input_path = os.path.join(day_dir, _INPUT_FILENAME)
        if os.path.isfile(input_path):
            with open(input_path, 'r') as fh:
                return fh.read()
    raise EnvironmentError('Could not find input file!')


def run_latest_solution(main_dir):
    """
    Grab the last/latest (by dir name) directory in main_dir that matches the
    pattern for problem directories(i.e. day\d{2}_\d{2}) that contains a solution.py

    also, oh god, since when did I even remotely think in regex.
    """

    days = {}

    for day_name in os.listdir(main_dir):
        day_path = os.path.join(main_dir, day_name)
        if not os.path.isdir(day_path):
            continue
        match = re.match(_DAY_RE_STR, day_name)
        if not match:
            continue
        day = int(match.groups()[0])

        if day in days:
            raise EnvironmentError("Duplicate day directories found for day {0}".format(day))

        days[day] = set()
        for problem_name in os.listdir(day_path):
            problem_path = os.path.join(day_path, problem_name)
            if not os.path.isdir(problem_path):
                continue
            if not problem_name.isdigit():
                continue

            solution_path = os.path.join(problem_path, _SOLUTION_FILENAME)
            if not os.path.isfile(solution_path):
                continue

            problem = int(problem_name)
            if problem in days[day]:
                raise EnvironmentError("Duplicate problem {0} found in day{1}!".format(problem, day))
            days[day].add(problem)
    for max_day, problems in sorted(days.items(), reverse=True):
        if problems:
            max_problem = max(problems)
            break

    return run_solution(main_dir, day=max_day, problem=max_problem)


def run_solution(main_dir, day, problem):
    problem_dir = _get_problem_dir(main_dir, day, problem)
    if problem_dir is None:
        day_dir = _get_day_dir(main_dir, day)
        if day_dir is None:
            msg = "Could not find a day directory for day {0}!".format(day)
        else:
            msg = "Could not find a problem directory for {0} in day {1}!".format(problem, day)
        sys.exit(msg)
    solution_filepath = os.path.join(problem_dir, _SOLUTION_FILENAME)
    if os.path.isfile(solution_filepath):
        sys.path.append(problem_dir)
        import solution

        input_val = get_input_for_problem(main_dir, day, problem)
        try:
            solution.run
        except AttributeError:
            raise EnvironmentError("The problem solution {0} does not contain a run() function!".format(solution_filepath))
        return solution.run(input_val)
    else:
        raise EnvironmentError("No solution exists for day {0} problem {1}".format(day, problem))




def run(day=None, problem=None):

    this_dir = os.path.dirname(__file__)
    try:
        if problem is None and problem is None:
            res = run_latest_solution(this_dir)

        elif day is not None and problem is not None:
            res = run_solution(this_dir, day=day, problem=problem)
        else:
            raise ValueError('You must provide both day and problem, or neither')
    except EnvironmentError as exc:
        sys.exit(repr(exc))


    print res


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if not len(sys.argv) == 3:
            sys.exit(_USAGE)
        day = int(sys.argv[1])
        problem= int(sys.argv[2])
        run(day=day, problem=problem)
    else:
        run()
