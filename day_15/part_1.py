from utils.geometry import *
import platform

base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_15.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_15_3.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def split_input(lines):
    empty_list = [i for i in range(len(lines)) if len(lines[i]) == 0][0]
    grid_lines = lines[:empty_list]
    moves = ''.join(lines[empty_list:])
    directions = []
    for i in moves:
        if i == '<':
            directions.append(Direction.W)
        elif i == '>':
            directions.append(Direction.E)
        elif i == '^':
            directions.append(Direction.N)
        elif i == 'v':
            directions.append(Direction.S)

    return grid_dict('\n'.join(grid_lines)), directions


def move(point, direction, grid):
    next_point = point + one_step(direction)
    if grid[next_point] == '.':
        grid[point] = '.'
        grid[next_point] = '@'
        return next_point
    elif grid[next_point] == '#':
        return point
    elif grid[next_point] == 'O':
        next_pos = point + one_step(direction)
        while True:
            if grid[next_pos] == 'O':
                next_pos += one_step(direction)
            elif grid[next_pos] == '#':
                return point
            elif grid[next_pos] == '.':
                grid[next_pos] = 'O'
                grid[next_point] = '@'
                grid[point] = '.'
                return next_point


def process(lines):
    grid, moves = split_input(lines)
    start = grid_position('@', grid)[0]

    for dir in moves:
        start = move(start, dir, grid)

    return sum([p.x + 100 * abs(p.y) for p in grid_position('O', grid)])


print("Sample output:", process(sample_lines))
# print("Answer:", process(input_lines))
