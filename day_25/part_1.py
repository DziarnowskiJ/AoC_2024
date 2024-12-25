import platform
from itertools import product

base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_25.txt', 'r') as file:
    input_lines = file.read()

with open(base_path + '/inputs/sample/sample_input_day_25.txt', 'r') as file:
    sample_lines = file.read()


def parse_input(lines):

    keys = []
    locks = []

    for struct in lines.split('\n\n'):
        part = struct.split('\n')
        transposed_struct = [''.join([row[i] for row in part]) for i in range(len(part[0]))]
        pins = [x.count('#') for x in transposed_struct]

        if struct[0][0] == '#':
            locks.append(pins)
        else:
            keys.append(pins)

    return keys, locks


def process(lines):
    keys, locks = parse_input(lines)
    key_lock_pairs = list(product(keys, locks))

    total = 0
    for key, lock in key_lock_pairs:
        if max([x + y for x, y in zip(key, lock)]) > 7:
            continue
        total += 1

    return total


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))
