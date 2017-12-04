
from __future__ import division


def _get_layer(n):
    for layer in range(n):
        layer_range = 1 + 8*n
        for layer_member in range():
            # TODO
            pass


def print_plot():
    lists = []
    for i in range(82):
        i += 1
        if i == 1:
            lists.append(0)
        elif i <= 9:
            lists.append(1)
        elif i <= 25:
            lists.append(2)
        elif i <= 49:
            lists.append(3)
        elif i <= 81:
            lists.append(4)

    print(lists)

def test():
    """
    Data from square 1 is carried 0 steps, since it's at the access port.
    Data from square 12 is carried 3 steps, such as: down, left, left.
    Data from square 23 is carried only 2 steps: up twice.
    Data from square 1024 must be carried 31 steps.
    """



    for row in range(10):
        print 
        assert _get_layer()

    assert run(1) == 0
    assert run(12) == 3
    assert run(23) == 2
    assert run(1024) == 31