import itertools

# For the problem, I could have done this with a dict dict[(x,y)] = val, but I like this better
class BidirectionalList(list):

    _NOT_SET = object()

    def __init__(self, zero_val=_NOT_SET):

        self._zero = zero_val
        self._pos_list = []
        self._neg_list = []

        super(BidirectionalList, self).__init__()

    def __getitem__(self, idx):

        if idx == 0:
            if self._zero is not self._NOT_SET:
                return self._zero
            else:
                raise IndexError('list index out of range')
        elif idx > 0:
            return self._pos_list[idx]
        elif idx < 0:
            return self._neg_list[idx * -1]
        else:
            # Should never get here
            assert False

    def __setitem__(self, idx, value):

        if idx == 0:
            self._zero = value
        elif self._zero == self._NOT_SET:
            raise IndexError('list assignment index out of range')
        elif idx < 0:
            self._neg_list[idx * -1] = value
        elif idx > 0:
            self._pos_list[idx] = value
        else:
            # should never get here
            assert False

    def __delitem__(self, idx):

        if self._pos_list or self._neg_list and idx == 0:
            msg = 'Cannot delete index 0 if there are other values in a BiDirectional List'
            raise IndexError(msg)
        elif idx > 0:
            del(self._pos_list[idx])

        elif idx < 0:
            del(self._neg_list[idx * -1])
        else:
            # should never get here
            assert False

    def __contains__(self, item):
        if self._zero != self._NOT_SET and item == self._zero:
            return True
        if item in self._pos_list or item in self._neg_list:
            return True

        return False

    def __len__(self):
        if self._zero is self._NOT_SET:
            return 0

        return 1 + len(self._pos_list) + len(self._neg_list)

    def __max__(self):
        all_list = self._pos_list + self._neg_list
        if self._zero is not self._NOT_SET:
            all_list.append(self._zero)
        return max(all_list)

    def __min__(self):
        all_list = self._pos_list + self._neg_list
        if self._zero is not self._NOT_SET:
            all_list.append(self._zero)
        return min(all_list)

    def __reversed__(self):
        if self._zero is not self._NOT_SET:
            for item in reversed(self._pos_list):
                yield item

            yield self._zero

            for item in self._neg_list:
                yield item

    def __iter__(self):
        if self._zero is not self._NOT_SET:
            for item in reversed(self._neg_list):
                yield item
            yield self._zero
            for item in self._pos_list:
                yield item

    def len_pos(self):
        if self._zero is self._NOT_SET:
            return 0

        return len(self._pos_list) + 1

    def len_neg(self):
        if self._zero is self._NOT_SET:
            return 0

        return len(self._neg_list) + 1


class CoordPlane(object):

    def __init__(self):
        self._list = BidirectionalList(zero_val=BidirectionalList())
        super(CoordPlane, self).__init__()

    def __setitem__(self, idx, value):
        x, y = idx
        self._list[x][y] = value

    def __getitem__(self, idx):
        x, y = idx
        return self._list[x][y]

    def __delitem__(self, idx):
        x, y = idx
        del(self._list[x][y])

    def __max__(self):

        return max(max(self._list))

    def __min__(self):

        return min(min(self._list))

    def is_square(self):
        # Doesn't actually check if square, checks if it's square and centered
        # on (0,0), but that works for my purposes.

        y_lens = set(len(col) for col in self._list)
        if not len(y_lens) == 1:
            return False

        if not len(self._list) == y_lens.pop():
            return False

        return True

    def get_min_max(self):

        max_x = self._list.len_pos()
        min_x = -self._list.len_neg()

        max_y = -float('inf')
        min_y = float('inf')

        for col in self._list:
            max_y = max(max_y, col.len_pos())
            min_y = min(min_y, -col.len_neg())

        return ((min_x, max_x), (min_y, max_y))

    def get_corners(self):

        x_range, y_range = self.get_min_max()
        return (
            (x_range[0], y_range[1]),
            (x_range[1], y_range[1]),
            (x_range[1], y_range[0]),
            (x_range[0], y_range[0]),
        )


    def print_grid(self):
        """
        For debugging.
        """

        val_pad_length = max(len(str(v)) for v in (max(self), min(self)))

        print max(self)
        print min(self)
        print val_pad_length

        x_range, y_range = self.get_min_max()
        idx_pad_length = max(len(str(v) for v in x_range + y_range))

        x_len = x_range[1] - x_range[0]
        y_len = y_range[1] - y_range[0]

        for i in range(y_range[1], y_range[0]-1, -1):
            pass




def _get_layer_count(spiral):
    assert spiral.is_square()

    x_range, y_range = spiral.get_min_max()

    # This is effectively part of spiral.is_square(), just an additional
    # check because I'm not actually performance-bound and I don't have
    # any sort of real tests up on the sprial class

    # Actually this is testing that the sprial centers on zero more than
    # anything else, which is not actually definitional in it being a
    # square, but is how I'm using it

    assert len(set(abs(v) for v in x_range + y_range)) == 1

    return x_range[1]


def _generate_spiral(to_layer, start_val=1, spiral=None):
    x = 0
    y = 0

    direction = (1, 0)

    if spiral is None:
        spiral = CoordPlane()
        spiral[0, 0] = start_val

    while _get_layer_count(spiral) < to_layer:
        _spiral_helper(spiral)

    return spiral

def _get_sum_of_surrounding(spiral, coord):
    total = 0
    for neighbor in itertools.product((-1, 0, 1), (-1, 0, 1)):
        print neighbor
        if neighbor == (0, 0):
            continue
        try:
            total += spiral[neighbor]
        except IndexError:
            continue

    return sum




def _spiral_helper(spiral):
    initial_corners = spiral.get_corners()

    pos = (initial_corners[2][0] + 1, initial_corners[2][1])
    directions = ((0, 1), (-1, 0), (0, -1), (1, 0))

    side_len = initial_corners[1][0] - initial_corners[0][0]
    for direction in directions:
        for _i in range(side_len):
            spiral[pos] = _get_sum_of_surrounding(spiral, pos)


def test():

    spiral = _generate_spiral(10)

    spiral.print_grid()

def run(in_val):
    in_val = int(in_val)
