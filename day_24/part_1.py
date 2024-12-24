import platform
from functools import cache

base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_24.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_24_3.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def parse_input(lines):
    empty = lines.index('')
    wires = {line[:3]: int(line[-1]) for line in lines[:empty]}
    ops = {line[-3:]: line[:-3].split(' ')[:3] for line in lines[empty + 1:]}

    return wires, ops


def get_wire(wire, wires, ops):
    if wire in wires:
        return int(wires[wire])
    else:
        op = ops[wire]
        if op[1] == 'AND':
            return get_wire(op[0], wires, ops) and get_wire(op[2], wires, ops)
        elif op[1] == 'OR':
            return get_wire(op[0], wires, ops) or get_wire(op[2], wires, ops)
        elif op[1] == 'XOR':
            return get_wire(op[0], wires, ops) ^ get_wire(op[2], wires, ops)


def process(lines):
    wires, ops = parse_input(lines)

    z_wires = [wire for wire in ops if wire.startswith('z')]
    z_wires_sorted = sorted(z_wires, key=lambda x: int(x[1:]))

    states = [get_wire(wire, wires, ops) for wire in reversed(z_wires_sorted)]
    return int('0b' + ''.join(list(map(str, states))), 2)


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))
