
def test():
    test_instructions = """0
3
0
1
-3"""
    assert run(test_instructions) == 10

def run(in_val):
    instructions = [int(instruction) for instruction in in_val.split()]
    offsets = {}

    register = 0
    steps = 0

    while True:
        try:
            instruction = instructions[register]
        except IndexError:
            return steps

        relative_offset = offsets.get(register, 0)
        offset = instruction + relative_offset

        if offset >= 3:
            offsets[register] = relative_offset - 1
        else:
            offsets[register] = relative_offset + 1

        register += offset
        steps += 1

