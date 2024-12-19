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


def process(lines, se, limit):
    grid = get_grid(lines, se, limit)
    path = bfs(origin, se, grid, diagonal=False)

    return len(path) - 1


print("Sample output:", process(sample_lines, Point(6, -6), 12))
print("Answer:", process(input_lines, Point(70, -70), 1024))
