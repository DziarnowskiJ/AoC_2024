import platform

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


def get_wire_string(wire, depth, wires, ops):
    def _get_wire(wire, depth):
        if depth == 0:
            return wire
        if wire in wires:
            return wire
        op = ops[wire]
        if op[1] == 'AND':
            return wire + '( ' + _get_wire(op[0], depth - 1) + ' & ' + _get_wire(op[2], depth - 1) + ' )'
        elif op[1] == 'OR':
            return wire + '( ' + _get_wire(op[0], depth - 1) + ' | ' + _get_wire(op[2], depth - 1) + ' )'
        elif op[1] == 'XOR':
            return wire + '( ' + _get_wire(op[0], depth - 1) + ' ^ ' + _get_wire(op[2], depth - 1) + ' )'

    return _get_wire(wire, depth)


def get_wire_val(wire, wires, ops):
    def _get_wire(wire):
        if wire in wires:
            return int(wires[wire])
        else:
            op = ops[wire]
            if op[1] == 'AND':
                return _get_wire(op[0]) and _get_wire(op[2])
            elif op[1] == 'OR':
                return _get_wire(op[0]) or _get_wire(op[2])
            elif op[1] == 'XOR':
                return _get_wire(op[0]) ^ _get_wire(op[2])

    return _get_wire(wire)


def swap_ops(op1, op2, ops):
    temp = ops[op2]
    ops[op2] = ops[op1]
    ops[op1] = temp


def get_sorted_states(letter, in_ops, ops, wires):
    l_wires = [wire for wire in (ops if in_ops else wires) if wire.startswith(letter)]
    l_wires_sorted = sorted(l_wires, key=lambda v: int(v[1:]))
    l_states = [get_wire_val(wire, wires, ops) for wire in reversed(l_wires_sorted)]
    return int('0b' + ''.join(list(map(str, l_states))), 2)


def process(lines):
    wires, ops = parse_input(lines)

    z_wires = [wire for wire in ops if wire.startswith('z')]
    z_wires_sorted = sorted(z_wires, key=lambda x: int(x[1:]))

    ops_to_swap = [
        # ('fph', 'z15'),     # bits 15-16
        # ('gds', 'z21'),     # bits 21-22
        # ('jrs', 'wrk'),     # bits 30-31
        # ('z34', 'cqk'),     # bits 34-35
    ]

    ops_to_swap = [
        ('z00', 'z05'),  # bits 15-16
        ('z01', 'z02'),  # bits 21-22
    ]

    for op1, op2 in ops_to_swap:
        swap_ops(op1, op2, ops)

    for z_wire in z_wires_sorted:
        print(get_wire_string(z_wire, 3, wires, ops))  # Useful to change between 2 and 3 for depth
    print()

    x_value = get_sorted_states('x', False, ops, wires)
    y_value = get_sorted_states('y', False, ops, wires)
    r_value = get_sorted_states('z', True, ops, wires)

    print('Actual values:')
    print('X value:       ', x_value)
    print('Y value:       ', y_value)
    print('Expected value:', x_value + y_value)
    print('Response value:', r_value)
    print()
    print('Binary values:')
    print('X value:       ', bin(x_value))
    print('Y value:       ', bin(y_value))
    print('Expected value:', bin(x_value + y_value))
    print('Response value:', bin(r_value))
    print('Compare bits right-to-left to determine which bit is faulty')
    print()

    sorted_ops = ','.join(sorted([item for tup in ops_to_swap for item in tup]))
    if r_value == x_value + y_value:
        return sorted_ops
    elif len(sorted_ops) > 0:
        return '(possible partial solution) ' + sorted_ops
    else:
        return '--No answer--'


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))
