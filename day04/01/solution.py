import util


def is_valid(password):
    words = password.split()
    return len(words) == len(set(str(sorted(word)) for word in words))


def test():

    invalid = [
        'abcde xyz ecdab',
        'oiii ioii iioi iiio'
    ]
    valid = [
        'abcde fghij',
        'a ab abc abd abf abj',
        'iiii oiii ooii oooi oooo',
    ]
    for t in invalid:
        assert not is_valid(t)
    for t in valid:
        assert is_valid(t)


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
