from utils.geometry import *
from utils.search import bfs
import platform

base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_18.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_18.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def get_grid(lines, se, limit):
    grid = empty_grid(origin, se)
    for line in lines[:limit]:
        x, y = line.split(',')
        del grid[Point(int(x), -int(y))]
    return grid


def process(lines, se):
    min_limit = 0
    max_limit = len(lines)

    while max_limit - min_limit > 1:
        temp_limit = (max_limit + min_limit) // 2

        grid = get_grid(lines, se, temp_limit)
        path = bfs(origin, se, grid, diagonal=False)
        if len(path) > 0:
            min_limit = temp_limit
        else:
            max_limit = temp_limit

    return lines[max_limit - 1]


print("Sample output:", process(sample_lines, Point(6, -6)))
print("Answer:", process(input_lines, Point(70, -70)))
