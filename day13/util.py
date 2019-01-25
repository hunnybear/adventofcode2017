

def test_run(firewall, start_time=0):

    # TODO
    pass

def advance_test(model):
    # TODO
    pass

def run_trip(firewall, start_y=0):
    depth = firewall.get_depth()

    score = 0

    for i in range(depth + 1):

        score += firewall.score_position(i, start_y)
        _print_firewall(firewall, (i, start_y))
        print('')
        firewall.advance()

        _print_firewall(firewall, (i, start_y))

        print('')
        print('-------------------------------------------------------------')
        print('')

    return score


def _print_firewall(firewall, track_pos=None):
    rows = []
    height = max(layer.range for layer in firewall.layers.values())

    while len(rows) < height:
        rows.append([])

    for y in range(height):
        for x in range(firewall.get_depth()):
            layer = firewall.layers.get(x)

            # state of firewall
            if layer is None:
                point_str = ' {0} '
            elif layer.pos == y:
                assert y < layer.range
                point_str = '({0})'
            elif y < layer.range:
                point_str = '[{0}]'
            else:
                point_str = ' {0} '

            if (x, y) == track_pos:
                point_str = point_str.format('*')

            else:
                point_str = point_str.format(' ')

            rows[y].append(point_str)

    for row in rows:
        print ' '.join(row)



class Layer(object):
    POSITIVE = 1
    NEGATIVE = -1

    def __init__(self, layer_range, start_pos=0):
        self.range = layer_range
        self.pos = start_pos
        self.direction = self.POSITIVE

        self.time = 0

        super(Layer, self).__init__()

    def advance(self):
        print self.direction, self.pos
        if self.direction == self.POSITIVE and self.pos + 1 == self.range:
            self.direction = self.NEGATIVE
        elif self.direction == self.NEGATIVE and self.pos == 0:
            self.direction == self.POSITIVE

        self.pos += self.direction

        self.time += 1


class Firewall(object):

    def __init__(self, layers):
        print layers
        self.layers = dict((depth, Layer(rng)) for depth, rng in layers.items())
        self.time = 0

        super(Firewall, self).__init__()

    def get_depth(self):
        return max(self.layers) + 1

    def advance(self):
        self.time += 1
        for layer in self.layers.values():
            layer.advance()
            assert self.time == layer.time

    def score_position(self, x, y):
        layer = self.layers.get(x)
        if layer is None:
            return 0

        if layer.pos == y:
            return layer.range * x

        return 0

