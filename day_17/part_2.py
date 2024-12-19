import re
import platform

base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_17.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]


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


def run(registers, program, A):
    reg = registers.copy()
    reg[4] = A
    pointer = 0
    out = []

    while True:
        if pointer >= len(program):
            return out

        op = program[pointer]
        val = program[pointer + 1]

        if op == 0:
            reg[4] = reg[4] // (2 ** get_combo(val, reg))
        elif op == 1:
            reg[5] = reg[5] ^ val
        elif op == 2:
            reg[5] = get_combo(val, reg) % 8
        elif op == 3:
            if reg[4] != 0:
                pointer = val
                continue
        elif op == 4:
            reg[5] = reg[5] ^ reg[6]
        elif op == 5:
            out.append(get_combo(val, reg) % 8)
        elif op == 6:
            reg[5] = reg[4] // (2 ** get_combo(val, reg))
        elif op == 7:
            reg[6] = reg[4] // (2 ** get_combo(val, reg))
        pointer += 2


def solve_A(registers, program, pointer, A):
    results = set()

    if pointer == -1:
        if program == run(registers, program, A >> 3):
            results.add(A >> 3)

    for x in range(8):
        out = run(registers, program, A + x)
        if out[0] == program[pointer]:
            results.update(solve_A(registers, program, pointer - 1, ((A + x) << 3)))

    return results


def process(lines):
    registers, program = split_input(lines)
    return min(solve_A(registers, program, len(program) - 1, 0))


print("Answer:", process(input_lines))
