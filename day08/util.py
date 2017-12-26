
import re

TEST_VALS = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""

IF = ' if '
INCREASE = 'inc'
DECREASE = 'dec'

CONDITION_OPERATORS = set(['==', '!=', '<', '<=', '>', '>='])

_action_re = '^(?P<register>[a-z]+)\s+(?P<action>(?:{0})|(?:{1}))\s+(?P<val>-?\d+)$'.format(INCREASE, DECREASE)
_condition_re = '^(?P<register>[a-z]+)\s+(?P<condition>.+?)$'.format('|'.join("(?:{0})".format(op) for op in CONDITION_OPERATORS))

def _execute_action(action, registers):

    re_match = re.match(_action_re, action)

    register = re_match.group('register')
    action = re_match.group('action')
    val = int(re_match.group('val'))

    if action == INCREASE:
        val = registers.get(register, 0) + val
    elif action == DECREASE:
        val = registers.get(register, 0) - val
    else:
        assert False

    registers[register] = val
    return val


def _check_condition(condition, registers):

    re_match = re.match(_condition_re, condition)

    register = re_match.group('register')
    condition = re_match.group('condition')

    assert register and condition

    register_val = registers.setdefault(register, 0)

    condition_string = '{0} {1}'.format(register_val, condition)

    return eval(condition_string)


def _execute_instruction(instruction, registers):
    """
    Siiiiide effects
    """

    action, condition = instruction.split(IF)
    if _check_condition(condition, registers):
        return _execute_action(action, registers)
    return None


def calc_registers(in_val):
    registers = {}
    max_value = -float('inf')
    for instruction in in_val.splitlines():
        res_val = _execute_instruction(instruction.strip(), registers)
        if res_val is not None:
            max_value = max([max_value, res_val])
    return registers, max_value
