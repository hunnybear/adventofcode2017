import util

def run(in_val):

    pos = util.get_position(in_val.strip().split(','))

    distance = max(abs(val) for val in pos)

    return distance


def test():
    """
    ne,ne,ne is 3 steps away.
    ne,ne,sw,sw is 0 steps away (back where you started).
    ne,ne,s,s is 2 steps away (se,se).
    se,sw,se,sw,sw is 3 steps away
    """

    _test_vals = {
        'ne,ne,ne': 3,
        'ne,ne,sw,sw': 0,
        'ne,ne,s,s': 2,
        'se,sw,se,sw,sw': 3,
    }

    for moves, expected_dist in _test_vals.items():
        dist = run(moves)

        assert dist == expected_dist
