import util


def test():
    #test_vals =
    assert run(util.TEST_VALS) == 'tknk'

def run(in_val):
    tree = util.parse_to_tree(in_val)

    return(tree.getroot().get(util.NAME))
