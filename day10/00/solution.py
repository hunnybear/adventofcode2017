import util

def test():

    test_vals = "3, 4, 1, 5"
    test_return = run(test_vals, loop_len=5)
    print test_return
    assert test_return == 12

def run(in_val, loop_len=256):

    skip_size = 0

    loop = util.Loop(range(loop_len))

    for length in [int(val) for val in in_val.strip().split(',')]:
        loop[0:length] = reversed(loop[0:length])
        loop.rotate(length + skip_size)
        skip_size += 1

    loop.reset_rotation()
    return loop[0] * loop[1]
