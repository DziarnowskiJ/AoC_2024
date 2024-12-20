from utils.geometry import *
from utils.search import dijkstra
from collections import defaultdict
import platform

base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_20.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_20.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def get_grid(lines):
    grid = grid_dict('\n'.join(lines))
    grid = {k: v for k, v in grid.items() if v != '#'}
    return grid


def get_index(ls, item):
    try:
        return ls.index(item)
    except ValueError:
        return -1


def process(lines, shortcut_length):
    grid = get_grid(lines)
    S = grid_position('S', grid)[0]
    E = grid_position('E', grid)[0]

    path, _ = dijkstra(S, E, grid, diagonal=False)

    shortcuts = []
    for i in range(len(path)):
        for d in [Direction.N, Direction.E, Direction.S, Direction.W]:
            after_cheat_index = get_index(path, path[i] + one_step(d).mul(2))
            if after_cheat_index > 0:
                shortcuts.append((path[i], path[after_cheat_index], after_cheat_index - i - 2))

    short_dict = defaultdict(int)
    for s in shortcuts:
        short_dict[s[2]] += 1

    total = sum([v for k, v in short_dict.items() if k >= shortcut_length])

    return total


print("Sample output:", process(sample_lines, 1))
print("Answer:", process(input_lines, 100))
