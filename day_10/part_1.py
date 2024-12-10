import platform
from utils.geometry import *

base_path = '..' if platform.python_implementation() == 'CPython' else '.'
with open(base_path + '/inputs/real/input_day_10.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_10.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def get_grid(lines):
    grid = grid_dict('\n'.join(lines))
    grid = {k: p for k, p in grid.items() if p != '.'}

    return grid


def process(lines):
    grid = get_grid(lines)
    start_points = grid_position('0', grid)

    counter = 0
    for start_point in start_points:
        neighs = [start_point]

        for i in range(1, 10):
            possible_locations = [*neighs]
            neighs = set()
            for neigh in possible_locations:
                # Possible steps
                neigh = set(key for key, val in get_neighbours_dict(neigh, grid, False).items() if
                             int(val) == int(grid[neigh]) + 1)
                neighs.update(neigh)
        possible_locations = [*neighs]
        counter += len(possible_locations)

    return counter


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))
