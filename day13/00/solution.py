import util

_TEST_INPUT = """0: 3
1: 2
4: 4
6: 4"""

def test():


    run(_TEST_INPUT)


def run(in_val):
    layer_inputs = dict((int(v.strip()) for v in line.split(':')) for line in in_val.splitlines() if line.strip)
    firewall = util.Firewall(layer_inputs)

    for depth, layer in firewall.layers.items():
        print depth, layer.range

    res = util.run_trip(firewall)
    print(res)
    return res
