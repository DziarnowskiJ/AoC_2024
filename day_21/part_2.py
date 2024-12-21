from utils.geometry import *
import platform
from functools import cache

base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_21.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_21.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

numeric_keypad = """789\n456\n123\n#0A"""
direction_keypad = """#^A\n<v>"""

numeric_grid = grid_dict(numeric_keypad)
numeric_grid = {key: val for key, val in numeric_grid.items() if val != '#'}

direction_grid = grid_dict(direction_keypad)
direction_grid = {key: val for key, val in direction_grid.items() if val != '#'}


def get_steps(start, end, pad_grid):
    start_point = grid_position(start, pad_grid)[0]
    end_point = grid_position(end, pad_grid)[0]

    dx, dy = (end_point - start_point).key

    vert = "v" * -dy + "^" * dy
    horiz = ">" * dx + "<" * -dx

    if dx > 0 and Point(start_point.x, end_point.y) in pad_grid:
        return vert + horiz + "A"
    elif Point(end_point.x, start_point.y) in pad_grid:
        return horiz + vert + "A"
    else:
        return vert + horiz + "A"


def get_clicks_numeric(path):
    route = []
    start = "A"
    for end in path:
        route.append(get_steps(start, end, numeric_grid))
        start = end
    return "".join(route)


def get_clicks_directions_from(start, path):
    route = []
    for end in path:
        route.append(get_steps(start, end, direction_grid))
        start = end
    return "".join(route)


@cache
def get_clicks(clicks, n):
    if n == 0:
        return len(clicks)

    start = 'A'
    res = 0
    for click in clicks:
        res += get_clicks(get_clicks_directions_from(start, click), n - 1)
        start = click

    return res


def process(lines):
    total = 0
    for line in lines:
        path = get_clicks_numeric(line)
        val = get_clicks(path, 25)
        total += int(line[:-1]) * val
    return total


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))
