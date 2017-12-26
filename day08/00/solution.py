import util

def run(in_val):
    registers, _max_value = util.calc_registers(in_val)
    return max(registers.values())


def test():
    res = run(util.TEST_VALS)
    assert res == 1
