from utils.geometry import *

with open('../inputs/real/input_day_6.txt', 'r') as file:
    lines = [i.rstrip("\n") for i in file.readlines()]

with open('../inputs/sample/sample_input_day_6.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def get_grid(lines):
    return grid_dict('\n'.join(lines))


def run_grid_with_obstacle(guard_pos, guard_dir, grid, obstacle):
    counter = dict()
    # Add obstacle to the grid
    grid[obstacle] = '#'

    while is_in_grid(guard_pos + one_step(guard_dir), grid):
        if grid[guard_pos + one_step(guard_dir)] == '#':
            guard_dir = turn_right(guard_dir)
        else:
            # If position was visited again with the same travel direction it means that path is looping
            if guard_pos in counter.keys():
                if guard_dir in counter[guard_pos]:
                    return obstacle
                counter[guard_pos].append(guard_dir)
            else:
                counter[guard_pos] = [guard_dir]
            guard_pos = guard_pos + one_step(guard_dir)
    return None


def get_path(grid):
    guard_pos = grid_position('^', grid)[0]
    guard_dir = Direction.N
    path = set()
    # Traverse through original grid and collect all distinct visited spots
    while is_in_grid(guard_pos + one_step(guard_dir), grid):
        if grid[guard_pos + one_step(guard_dir)] == '#':
            guard_dir = turn_right(guard_dir)
        else:
            guard_pos = guard_pos + one_step(guard_dir)
            path.add(guard_pos)

    return path


def process(line):
    grid = get_grid(line)
    possible_places = get_path(grid)
    guard_pos = grid_position('^', grid)[0]
    guard_dir = Direction.N

    obstacles = set()

    for p in possible_places:
        # Try to traverse the grid, if path loops add obstacle to the obstacle list
        obstacles.add(run_grid_with_obstacle(guard_pos, guard_dir, grid.copy(), p))

    obstacles.remove(None)
    return len(obstacles)


print("Sample output:", process(sample_lines))
print("Answer:", process(lines))
