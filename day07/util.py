
# TODO switch to cElementTree when I don't care about autocomplete anymore
from xml.etree import ElementTree
import re

_parse_re_str = '^([a-zA-z]*)\s+\((\d+)\)(?:\s+->\s+((?:\w+, )*\w+))?$'

NAME = 'name'
WEIGHT = 'weight'

TEST_VALS = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
"""


def parse_to_tree(in_val):
    elements = {}

    for entry in in_val.splitlines():
        if not entry:
            continue
        name, weight, children = re.match(_parse_re_str, entry).groups()

        #print name, weight, children
        if children is not None:
            children = [child.strip().rstrip(',') for child in children.split()]

        assert name not in elements
        element = ElementTree.Element('tower', attrib={NAME: name, WEIGHT: int(weight)})

        elements[name] = (element, children or [])

    #print elements
    possible_roots = set(elements)

    for element, children in elements.values():
        possible_roots.difference_update(children)
        #print children
        for child in children:
            element.append(elements[child][0])
    assert len(possible_roots) == 1

    tree = ElementTree.ElementTree(elements[possible_roots.pop()][0])

    return tree


