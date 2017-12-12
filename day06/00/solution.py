
import util

def test():

    assert run("0 2 7 0") == 5


def run(in_val):

    seen, _dupe_idx = util.get_cycles(in_val)

    return len(seen)
