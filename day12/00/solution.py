import re

import util

_TEST_INVAL  = """
0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
"""

_PIPE_RE = "^(\d+)\s+<->\s+((?:\d+, )*\d+)$"


_TEST_PIPES = {
    0: set([2]),
    1: set([1]),
    2: set([0, 3, 4]),
    3: set([2, 4]),
    4: set([2, 3, 6]),
    5: set([6]),
    6: set([4, 5]),
}

def run(in_val):
    pipes = {}

    for line in in_val.splitlines():
        if not line.strip():
            continue

        match = re.match(_PIPE_RE, line.strip())
        assert match

        source, connections = match.groups()

        pipes[int(source)] = set(int(i) for i in connections.split(', '))

    islands = util.get_islands(pipes)

    # Theres a much better way to do this inline, but I'm not in a
    # big rush here

    for island in islands:
        if 0 in island:
            break

    else:
        assert False

    return len(island)



def test():

    islands = run(_TEST_INVAL)

    for island in islands:
        print island
        print ""
