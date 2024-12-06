from utils.geometry import *

with open('../inputs/real/input_day_6.txt', 'r') as file:
    lines = [i.rstrip("\n") for i in file.readlines()]

with open('../inputs/sample/sample_input_day_6.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def get_grid(lines):
    return grid_dict('\n'.join(lines))


def process(line):
    grid = get_grid(line)
    guard_pos = grid_position('^', grid)[0]
    grid[guard_pos] = 'X'
    guard_dir = Direction.N
    counter = 1
    while is_in_grid(guard_pos + one_step(guard_dir), grid):
        if grid[guard_pos + one_step(guard_dir)] == '#':
            guard_dir = Direction((guard_dir + 2) % 8)
        else:
            grid[guard_pos] = 'X'
            guard_pos = guard_pos + one_step(guard_dir)
            if grid[guard_pos] != 'X':
                counter += 1

    return counter

print("Sample output:", process(sample_lines))
print("Answer:", process(lines))

