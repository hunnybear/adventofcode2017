import itertools

# For the problem, I could have done this with a dict dict[(x,y)] = val, but I like this better

class CoordPlane(object):

    def __init__(self):
        self._coords = {}
        super(CoordPlane, self).__init__()

    def __setitem__(self, idx, value):
        x, y = idx
        if x in self._coords:
            assert y not in self._coords[x]
        self._coords.setdefault(x, {})[y] = value

    def __getitem__(self, idx):
        x, y = idx
        return self._coords[x][y]

    def __delitem__(self, idx):
        x, y = idx
        del(self._coords[x][y])

    def __iter__(self):

        for x in self._coords:
            for y in self._coords[x]:
                yield self._coords[x][y]

    def is_square(self):
        # Doesn't actually check if square, checks if it's square and centered
        # on (0,0), but that works for my purposes.

        x_range, y_range = self.get_min_max()

        if x_range != y_range:
            return False

        if abs(x_range[0]) != x_range[1]:
            return False

        # This is a little brute forcey, but since I'm not using the
        # bidirectional list idea anymore, just trying to knock it out easily.

        for x in range(x_range[0], x_range[1] + 1):
            for y in range(y_range[0], y_range[1] + 1):
                try:
                    self._coords[x][y]
                except IndexError:
                    return False

        return True



    def get_min_max(self):

        max_x = max(self._coords)
        min_x = min(self._coords)

        max_y = -float('inf')
        min_y = float('inf')

        for col in self._coords.values():
            max_y = max(max_y, max(col))
            min_y = min(min_y, min(col))

        return ((min_x, max_x), (min_y, max_y))

    def get_corners(self):

        x_range, y_range = self.get_min_max()
        return (
            (x_range[0], y_range[1]),
            (x_range[1], y_range[1]),
            (x_range[1], y_range[0]),
            (x_range[0], y_range[0]),
        )


    def get_grid_string(self):
        """
        For debugging.
        """

        grid_rows = []


        val_pad_length = max(len(str(v)) for v in (max(self), min(self)))

        x_range, y_range = self.get_min_max()
        idx_pad_length = max(len(str(v)) for v in x_range + y_range)
        pad_length = max([val_pad_length, idx_pad_length])

        x_len = x_range[1] - x_range[0]
        y_len = y_range[1] - y_range[0]


        for y in range(y_range[1], y_range[0] - 1, -1):
            grid_row = "{0:<{pad}}\t".format(y, pad=idx_pad_length)


            for x in range(x_range[0], x_range[1] + 1):
                try:
                    val = self._coords[x][y]
                except KeyError:
                    val = '-'
                val_line = "{0:>{align}}  ".format(val, align=pad_length)

                grid_row += val_line
            grid_rows.append(grid_row)

        grid_rows.append("")

        col_key = " " * idx_pad_length + "\t"
        col_idxs = ["{0:>{pad}}".format(idx, pad=idx_pad_length) for idx in range(x_range[0], x_range[1] + 1)]

        col_key += "  ".join(col_idxs)

        grid_rows.append(col_key)

        return '\n'.join(grid_rows)




    def __str__(self):
        return self.get_grid_string()


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


def _generate_spiral(to_val, start_val=1, spiral=None):

    if spiral is None:
        spiral = CoordPlane()
        spiral[0, 0] = start_val

    spiral_val_count = 0
    do_continue = True
    while do_continue:
        do_continue = False
        for val in _spiral_helper(spiral):
            spiral_val_count += 1
            if val > to_val:
                break
        else:
            do_continue = True

    return spiral, spiral_val_count, val

def _get_sum_of_surrounding(spiral, coord):
    total = 0
    for neighbor_offset in itertools.product((-1, 0, 1), (-1, 0, 1)):
        if neighbor_offset == (0, 0):
            continue
        neighbor = (coord[0] + neighbor_offset[0], coord[1] + neighbor_offset[1])
        try:
            total += spiral[neighbor]
        except KeyError:
            continue

    return total


def _spiral_helper(spiral):
    initial_corners = spiral.get_corners()

    pos = (initial_corners[2][0] + 1, initial_corners[2][1])
    directions = ((0, 1), (-1, 0), (0, -1), (1, 0))

    side_len = initial_corners[1][0] - initial_corners[0][0] + 1

    first_side = True
    for direction in directions:
        if direction == directions[-1]:
            side_len += 1
        for _i in range(side_len):
            pos_val = _get_sum_of_surrounding(spiral, pos)
            # holy side effects, batman!
            spiral[pos] = pos_val
            yield pos_val
            pos = (pos[0] + direction[0], pos[1] + direction[1])

        if first_side:
            first_side = False
            side_len += 1
    # handle teh last side

    # TOREMOVE
    #print("dict:")
    #print spiral._coords
    #print("formatted:")
    #print spiral



def test():

    spiral, steps = _generate_spiral(5)

    print(spiral)

    spiral, steps = _generate_spiral(250)

    print(spiral)


def run(in_val):
    in_val = int(in_val)
    val = _generate_spiral(to_val=in_val)
    return val
