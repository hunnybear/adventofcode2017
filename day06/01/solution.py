import util

def test():
    print(run("0 2 7 0"))
    assert run("0 2 7 0") == 4


def run(in_val):
    cycles, dupe_index = util.get_cycles(in_val)

    return len(cycles) - dupe_index

