import util

_weight_cache = {}


def _get_weight(element):
    if element not in _weight_cache:
        child_weights = sum([_get_weight(child) for child in element])
        _weight_cache[element] = element.get(util.WEIGHT) + child_weights
    return _weight_cache[element]


def _print_sub_weights(sub_weights):

    for el, weight in sub_weights.items():
        print "\t{0}: {1}".format(el.get(util.NAME), weight)


def run(in_val):

    tree = util.parse_to_tree(in_val)

    sub_weights = dict((el, _get_weight(el)) for el in tree.getroot())

    new_weight = None

    # This is all a bit messy, could live with refactoring
    while len(set(sub_weights.values())) != 1:
        all_weights = set(sub_weights.values())
        for el, weight in sub_weights.items():
            if sub_weights.values().count(weight) == 1:
                other_weight = all_weights.difference(set([weight])).pop()

                if len(el):
                    # recalc sub_weights
                    sub_weights = dict((child_el, _get_weight(child_el)) for child_el in el)
                    new_weight = other_weight - sum(sub_weights.values())

                    break

                else:
                    return other_weight

                break

    assert new_weight is not None
    return new_weight


def test():
    res = run(util.TEST_VALS)
    print(res)
    assert res == 60
