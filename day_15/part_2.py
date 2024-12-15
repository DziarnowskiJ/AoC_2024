from utils.geometry import *
import platform

base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_15.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_15_3.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def split_input(lines):
    empty_list = [i for i in range(len(lines)) if len(lines[i]) == 0][0]
    grid_lines = '\n'.join(lines[:empty_list]) \
        .replace('#', '##') \
        .replace('O', '[]') \
        .replace('.', '..') \
        .replace('@', '@.')
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

    return grid_dict(grid_lines), directions


def swap_box(point, grid):
    if grid[point] == '[':
        grid[point] = ']'
    elif grid[point] == ']':
        grid[point] = '['


def move(point, direction, grid):
    next_point = point + one_step(direction)
    if grid[next_point] == '.':
        grid[point] = '.'
        grid[next_point] = '@'
        return next_point
    elif grid[next_point] == '#':
        return point
    elif grid[next_point] in ['[', ']']:
        # Horizontal moves
        if direction in [Direction.W, Direction.E]:
            next_pos = point + one_step(direction)
            moved_boxes = []
            while is_in_grid(next_pos, grid):
                if grid[next_pos] in ['[', ']']:
                    moved_boxes.append(next_pos)
                    next_pos += one_step(direction)
                elif grid[next_pos] == '#':
                    return point
                elif grid[next_pos] == '.':
                    grid[next_point] = '@'
                    grid[next_pos] = '[' if direction == Direction.W else ']'
                    grid[point] = '.'
                    [swap_box(p, grid) for p in moved_boxes]
                    return next_point
        # Vertical moves
        elif direction in [Direction.N, Direction.S]:
            points_to_check = {next_point}
            if grid[next_point] == '[':
                points_to_check.add(next_point + one_step(Direction.E))
            elif grid[next_point] == ']':
                points_to_check.add(next_point + one_step(Direction.W))

            moved_boxes = points_to_check
            next_poses = {p + one_step(direction) for p in points_to_check}

            while True:
                if any([grid[p] == '#' for p in next_poses]):
                    return point
                elif all([grid[p] == '.' for p in next_poses]):

                    old_boxes = {p: grid[p] for p in moved_boxes}

                    for p in old_boxes.keys():
                        grid[p] = '.'
                    for p, v in old_boxes.items():
                        grid[p + one_step(direction)] = v

                    grid[point] = '.'
                    grid[next_point] = '@'
                    return next_point
                elif any([grid[p] in ['[', ']']] for p in next_poses):
                    new_poses = set()
                    for p in next_poses:
                        if grid[p] == '[':
                            new_poses.add(p + one_step(Direction.E) + one_step(direction))
                            moved_boxes.add(p + one_step(Direction.E))
                            moved_boxes.add(p)
                            new_poses.add(p + one_step(direction))
                        elif grid[p] == ']':
                            new_poses.add(p + one_step(Direction.W) + one_step(direction))
                            moved_boxes.add(p + one_step(Direction.W))
                            moved_boxes.add(p)
                            new_poses.add(p + one_step(direction))
                    next_poses = new_poses


def process(lines):
    grid, moves = split_input(lines)
    start = grid_position('@', grid)[0]

    print(points_to_text(grid))
    print()
    for i, dir in enumerate(moves):
        start = move(start, dir, grid)
        print(points_to_text(grid))
        print()

    return sum([p.x + 100 * abs(p.y) for p in grid_position('[', grid)])


print("Sample output:", process(sample_lines))
# print("Answer:", process(input_lines))
