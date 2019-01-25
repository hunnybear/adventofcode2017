"""

        x

  z   \ n  /    y (+x, -z)
    nw +--+ ne
      /    \
    -+      +-
      \    /
    sw +--+ se
  y   / s  \    z (+x, -y)

        x (-y, +z)

"""
_MOVES = {
    'ne': (1, 0, -1),
    'se': (1, -1, 0),
    'n': (0, 1, -1),
    's': (0, -1, 1),
    'nw': (-1, 1, 0),
    'sw': (-1, 0, 1),
}

def get_position(path, pos=(0, 0, 0)):

    for move in path:
        pos = tuple(sum(vals) for vals in zip(pos, _MOVES[move.lower()]))
        assert not sum(pos)

    return pos

