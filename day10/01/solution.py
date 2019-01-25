import util

_SUFFIX_LENGTHS = [17, 31, 73, 47, 23]
HASH_DIVISOR = 16

def test():

    """
The empty string becomes a2582a3a0e66e6e86e3812dcb672a272.
AoC 2017 becomes 33efeb34ea91902bb2f59c9920caa6cd.
1,2,3 becomes 3efbe78a8d82f29979031a4aa0b16a9d.
1,2,4 becomes 63960835bcdc130f0b66d7ff4f6a5a8e.
    """

    tests = {
        '': 'a2582a3a0e66e6e86e3812dcb672a272',
        'AoC 2017': '33efeb34ea91902bb2f59c9920caa6cd',
        '1,2,3': '3efbe78a8d82f29979031a4aa0b16a9d',
        '1,2,4': '63960835bcdc130f0b66d7ff4f6a5a8e'
    }

    for inval, correct in tests.items():
        hashval = run(inval)
        print hashval
        print correct
        assert hashval == correct
        print ''


def _get_dense_hash(sparse_hash):
    dense_hash = []

    assert not len(sparse_hash) % HASH_DIVISOR

    for i in range(len(sparse_hash) / HASH_DIVISOR):
        hash_slice = sparse_hash[i * HASH_DIVISOR: (i + 1) * HASH_DIVISOR]
        dense_hash.append(reduce(lambda x, y: x ^ y, hash_slice))

    return dense_hash

def run(in_val, loop_len=256, rounds=64):

    skip_size = 0

    loop = util.Loop(range(loop_len))

    lengths = [ord(char) for char in in_val.rstrip()] + _SUFFIX_LENGTHS
    for _rnd in range(rounds):
        for length in lengths:
            loop[0:length] = reversed(loop[0:length])
            loop.rotate(length + skip_size)
            skip_size += 1

    loop.reset_rotation()
    dense_hash = _get_dense_hash(loop)

    hex_hash = ''.join('{0:02x}'.format(int(val)) for val in dense_hash)
    return hex_hash
