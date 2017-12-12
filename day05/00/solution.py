
def test():
    test_instructions = """0
3
0
1
-3"""
    assert run(test_instructions) == 5

def run(in_val):
    instructions = [int(instruction) for instruction in in_val.split()]
    rel_offsets = {}

    register = 0
    steps = 0

    while True:
        try:
            instruction = instructions[register]
        except IndexError:
            return steps

        offset = rel_offsets.get(register, 0)

        rel_offsets[register] = offset + 1
        register += instruction + offset

        steps += 1

