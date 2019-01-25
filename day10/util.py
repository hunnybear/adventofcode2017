import sys

class Loop(list):

    def __init__(self, val):
        self._start = 0
        super(Loop, self).__init__(val)

    def __getitem__(self, idx):

        if idx < 0:
            raise IndexError("Loops do not support negative indexing")
        loop_idx = self._getindex(idx)
        return super(Loop, self).__getitem__(loop_idx)

    def __iter__(self):
        for i in self[0:sys.maxint]:
            yield i

    def __repr__(self):
        return str(list(self))

    def reset_rotation(self):
        self._start = 0

    def get_position(self):
        return self._start

    def _getindex(self, idx):
        return (idx + self._start) % len(self)


    def _get_slice_indices(self, i, j):
        indices = []

        if i == j:
            return indices

        if j == sys.maxint:
            end = self._start
        else:
            end = self._getindex(j)

        start = self._getindex(i)

        if start >= end:
            indices.append((start, len(self)))
            if end > 0:
                indices.append((0, end))

        else:
            indices.append((start, end))

        return indices

    def __getslice__(self, i, j):

        this_slice = []

        indices = self._get_slice_indices(i, j)
        for slice_seg in indices:
            this_slice += super(Loop, self).__getslice__(slice_seg[0], slice_seg[1])
        return this_slice

    def __setslice__(self, i, j, sequence):
        indices = self._get_slice_indices(i, j)

        if indices:
            del(self[i: j])
        else:
            assert i == j
            idx = self._getindex(i)
            indices = [(idx, idx+1)]

        sequence_add = list(sequence)
        add_idxs = sum([range(start, end) for start, end in indices], [])

        while len(add_idxs) < len(sequence_add):
            add_idxs.append(add_idxs[-1] + 1)

        # Trim add_idxs, if needed
        add_idxs = add_idxs[:len(sequence_add)]

        for insert_idx, val in zip(add_idxs, sequence_add):
            self.insert(insert_idx, val)

    def __delslice__(self, i, j):

        indices = self._get_slice_indices(i, j)

        for slice_seg in indices:
            super(Loop, self).__delslice__(slice_seg[0], slice_seg[1])


    def rotate(self, rotate_by=1):
        self._start = (self._start + rotate_by) % len(self)






