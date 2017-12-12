import util


def is_valid(password):
    words = password.split()
    return len(words) == len(set(words))


def test():
    assert is_valid('aa bb cc dd ee')
    assert not is_valid('aa bb cc dd aa')
    assert is_valid('aa bb cc dd aaa')


def run(in_val):
    valid_counter = 0
    invalid_counter = 0
    for password in util.get_passwords(in_val):
        if is_valid(password):
            valid_counter += 1
        else:
            invalid_counter += 1

    print invalid_counter

    return valid_counter
