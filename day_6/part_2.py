from utils.geometry import *

with open('../inputs/real/input_day_6.txt', 'r') as file:
    lines = [i.rstrip("\n") for i in file.readlines()]

with open('../inputs/sample/sample_input_day_6.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def get_grid(lines):
    return grid_dict('\n'.join(lines))


def run_grid_with_obstacle(guard_pos, guard_dir, line, obstacle):
    counter = dict()
    grid = get_grid(line)
    grid[obstacle] = '#'

    while is_in_grid(guard_pos + one_step(guard_dir), grid):
        if grid[guard_pos + one_step(guard_dir)] == '#':
            guard_dir = turn_right(guard_dir)
        else:
            if guard_pos in counter.keys():
                counter[guard_pos] += 1
                if counter[guard_pos] > 4:
                    return obstacle
            else:
                counter[guard_pos] = 1
            guard_pos = guard_pos + one_step(guard_dir)
    return


def get_path(line):
    grid = get_grid(line)
    guard_pos = grid_position('^', grid)[0]
    grid[guard_pos] = 'X'
    guard_dir = Direction.N
    counter = set()
    while is_in_grid(guard_pos + one_step(guard_dir), grid):
        if grid[guard_pos + one_step(guard_dir)] == '#':
            guard_dir = turn_right(guard_dir)
        else:
            grid[guard_pos] = 'X'
            guard_pos = guard_pos + one_step(guard_dir)
            counter.add(guard_pos)

    return counter


def process(line):
    grid = get_grid(line)
    possible_places = get_path(line)
    guard_pos = grid_position('^', grid)[0]
    guard_dir = Direction.N

    obstacles = set()

    for p in possible_places:
        # Add obstacle
        grid[p] = '#'
        obstacles.add(run_grid_with_obstacle(guard_pos, guard_dir, line, p))

    obstacles.remove(None)
    return len(obstacles)


print("Sample output:", process(sample_lines))
print("Answer:", process(lines))
