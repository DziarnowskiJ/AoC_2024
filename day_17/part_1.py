import re
import platform

base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_17.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_17.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def split_input(lines):
    registers = {
        4: int(re.findall(r"\d+", lines[0])[0]),
        5: int(re.findall(r"\d+", lines[1])[0]),
        6: int(re.findall(r"\d+", lines[2])[0])
    }
    program = [int(i) for i in re.findall(r"\d+", lines[4])]

    return registers, program


def get_combo(val, registers):
    return val if val < 4 else registers[val]


def run(registers, program):
    pointer = 0
    out = []

    while True:
        if pointer >= len(program):
            return out

        op = program[pointer]
        val = program[pointer + 1]
        combo = get_combo(val, registers)

        if op == 0:
            registers[4] = registers[4] // (2 ** combo)
        elif op == 1:
            registers[5] = registers[5] ^ val
        elif op == 2:
            registers[5] = combo % 8
        elif op == 3:
            if registers[4] != 0:
                pointer = val
                continue
        elif op == 4:
            registers[5] = registers[5] ^ registers[6]
        elif op == 5:
            out.append(str(combo % 8))
        elif op == 6:
            registers[5] = registers[4] // (2 ** combo)
        elif op == 7:
            registers[6] = registers[4] // (2 ** combo)
        pointer += 2


def process(lines):
    registers, program = split_input(lines)
    result = run(registers, program)
    return ','.join([str(x) for x in result])


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))
