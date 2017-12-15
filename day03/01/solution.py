
class BidirectionalList(list):

    _NOT_SET = object()

    def __init__(self, zero_val=_NOT_SET):

        self._zero = zero_val
        self.pos_list = []
        self.neg_list = []

        super(BidirectionalList, self).__init__()

    def __getitem__(self, idx):

        if idx == 0:
            if self._zero is not self._NOT_SET:
                return self._zero
            else:
                raise IndexError('list index out of range')
        elif idx > 0:
            return pos_list[idx]
        elif idx < 0:
            return neg_list[idx * -1]
        else:
            # Should never get here
            assert False

    def __setitem__(self, idx, value):

        if idx == 0:
            self._zero = value
        elif self._zero == self._NOT_SET:
            raise IndexError('list assignment index out of range')
        elif idx < 0:
            self.neg_list[idx * -1] = value
        elif idx > 0:
            self.pos_list[idx] = value
        else:
            # should never get here
            assert False

    def __delitem__(self, idx):

        if self.pos_list or self.neg_list and idx == 0:
            msg = 'Cannot delete index 0 if there are other values in a BiDirectional List'
            raise IndexError(msg)
        elif idx > 0:
            del(self.pos_list[idx])

        elif idx < 0:
            del(self.neg_list[idx * -1])
        else:
            # should never get here
            assert False

    def __contains__(self, item):
        if self._zero != self._NOT_SET and item == self._zero:
            return True
        if item in self.pos_list or item in self.neg_list:
            return True

        return False

    def __len__(self, item):
        if self._zero is self._NOT_SET:
            return 0

        return 1 + len(self.pos_list) + len(self.neg_list)

    def __reversed__(self):
        if self._zero is not self._NOT_SET:
            for item in reversed(self.pos_list):
                yield item

            yield self._zero

            for item in self.neg_list:
                yield item

    def __iter__(self):
        if self._zero is not self._NOT_SET:
            for item in reversed(self.neg_list):
                yield item
            yield self._zero
            for item in self.pos_list:
                yield item


class CoordPlane(object):

    def __init__(self, starting_value=1):
        self._list = BidirectionalList(zero_val=BidirectionalList(zero_val=starting_value))
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

    def is_square(self):
        y_lens = set(len(col) for col in self._list)
        if not len(y_lens) == 1:
            return False

        if not len(self._list) == y_lens.pop():
            return False

        return True


def _generate_spiral(start_val=1):
    x = 0
    y = 0

    direction = (1, 0)

    spiral = []

    while True:
        if not spiral:
            spiral.append([start_val])
            continue





def run(in_val):
    in_val = int(in_val)
