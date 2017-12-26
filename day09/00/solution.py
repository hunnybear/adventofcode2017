import util

def run(in_val):
    return util.read_stream(in_val)[0]


def test():
    """
    {}, score of 1.
    {{{}}}, score of 1 + 2 + 3 = 6.
    {{},{}}, score of 1 + 2 + 2 = 5.
    {{{},{},{{}}}}, score of 1 + 2 + 3 + 3 + 3 + 4 = 16.
    {<a>,<a>,<a>,<a>}, score of 1.
    {{<ab>},{<ab>},{<ab>},{<ab>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
    {{<!!>},{<!!>},{<!!>},{<!!>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
    {{<a!>},{<a!>},{<a!>},{<ab>}}, score of 1 + 2 = 3.
    """

    tests = {
        '{}': 1,
        '{{{}}}': 6,
        '{{},{}}': 5,
        '{{{},{},{{}}}}': 16,
        '{<a>,<a>,<a>,<a>}': 1,
        '{{<ab>},{<ab>},{<ab>},{<ab>}}': 9,
        '{{<!!>},{<!!>},{<!!>},{<!!>}}': 9,
        '{{<a!>},{<a!>},{<a!>},{<ab>}}': 3,
    }

    for stream, target_score in tests.items():
        score = run(stream)
        print stream, target_score, score
        assert target_score == score

