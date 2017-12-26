import util

def run(in_val):
    _registers, max_value = util.calc_registers(in_val)
    return max_value


def test():
    res = run(util.TEST_VALS)
    assert res == 10
