
from __future__ import division

import math

def _get_layer_helper(n):
    pass

def _get_layer_info(n):

    last_len = 1
    current_layer = 0
    current_n = 1  # This will be the last n for the tested layer

    while current_n < n:
        current_layer += 1
        if last_len < 8:
            last_len = 8
        else:
            last_len = last_len + 8
        current_n += last_len


    start_n = current_n - last_len + 1

    return current_layer, start_n, current_n, last_len


def _get_layer_corners(start, end, layer_len=None):

    # compute len if it's not passed in, otherwise
    # assume passed in len is correct

    if layer_len is None:
        layer_len = end - start + 1

    corner_dist = layer_len / 4

    # this range is 3,2,1,0, so range(4) reversed
    for corner_n in range(3, -1, -1):
        yield end - (corner_dist * corner_n)


def _get_dist(n):

    layer, layer_start, layer_end, layer_len = _get_layer_info(n)

    corners = _get_layer_corners(layer_start, layer_end, layer_len=layer_len)

    dist_from_corner = min(abs(corner - n) for corner in corners)

    dist = layer + layer - dist_from_corner

    return dist


def get_plot():
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

    return(lists)


def test():
    """
    Data from square 1 is carried 0 steps, since it's at the access port.
    Data from square 12 is carried 3 steps, such as: down, left, left.
    Data from square 23 is carried only 2 steps: up twice.
    Data from square 1024 must be carried 31 steps.
    """



    for i, correct_layer in enumerate(get_plot(), 1):
        found_layer, start, end, layer_len = _get_layer_info(i)
        #print i, found_layer, correct_layer, start, end, layer_len
        assert found_layer == correct_layer

    assert run(1) == 0
    assert run(12) == 3
    assert run(23) == 2
    print(run(1024))
    assert run(1024) == 31

def run(inval):
    return _get_dist(int(inval))
