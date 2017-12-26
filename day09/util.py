TEST_GARBAGE = set([
    '<>',
    '<random characters>',
    '<<<<>',
    '<{!>}>',
    '<!!>',
    '<!!!>>',
    '<{o"i!a,<{i<a>'
])

GARBAGE_START = '<'
GARBAGE_END = '>'
GARBAGE_CANCEL = '!'

GROUP_START = '{'
GROUP_END = '}'


def _get_group_score(depth):
    if depth == 1:
        return 1
    elif depth < 1:
        assert False
    return _get_group_score(depth - 1) + 1


def read_stream(stream):

    depth = 0
    in_garbage = False
    cancel = False
    last_char = None

    score = 0
    garbage_count = 0

    for val in stream:
        count_garbage = True

        if cancel:
            cancel = False

        elif val == GARBAGE_CANCEL:
            cancel = True


        elif in_garbage:

            if val == GARBAGE_END:
                in_garbage = False
            else:
                garbage_count += 1


        elif val == GROUP_START:
            depth += 1

        elif val == GROUP_END:
            assert depth
            group_score =_get_group_score(depth)

            score += group_score
            depth -= 1

        elif val == GARBAGE_START:
            in_garbage = True

        elif val == ',':
            assert last_char in (GROUP_END, GARBAGE_END)

        else:
            print ("bad char: " + val)
            assert False

        last_char = val

    return score, garbage_count

