import util

def run(in_val):
    return util.read_stream(in_val)[1]


def test():
    """
    <>, 0 characters.
<random characters>, 17 characters.
<<<<>, 3 characters.
<{!>}>, 2 characters.
<!!>, 0 characters.
<!!!>>, 0 characters.
<{o"i!a,<{i<a>, 10 characters.
    """

    tests = {
        '<>': 0,
        '<random characters>': 17,
        '<<<<>': 3,
        '<{!>}>': 2,
        '<!!>': 0,
        '<!!!>>': 0,
        '<{o"i!a,<{i<a>': 10,
    }

    for stream, target_score in tests.items():
        score = run(stream)
        print stream, target_score, score
        assert target_score == score

