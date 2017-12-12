
def test():

    assert run("0 2 7 0") == 5


def run(in_val):

    banks = [int(v) for v in in_val.split()]
    seen = []

    while banks not in seen:
        seen.append(list(banks))
        high_mem = max(banks)
        highest_idx = banks.index(high_mem)
        banks[highest_idx] = 0
        for idx in range(high_mem):
            bank_idx = (highest_idx + idx + 1) % len(banks)
            banks[bank_idx] += 1

    return len(seen)
