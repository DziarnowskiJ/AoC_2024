from utils.geometry import *
import platform

base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_12.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_12.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def get_grid(lines):
    return grid_dict('\n'.join(lines))


def get_area(point, grid):
    location = point
    area = {location: grid[location]}

    to_check = {location}

    # BFS to get all neighbours of the same type
    while to_check:
        check = to_check.pop()
        check_val = grid[check]
        for neighbour in [neigh for neigh, val in get_neighbours_dict(check, grid, False).items() if val == check_val]:
            if neighbour not in area:
                to_check.add(neighbour)
            area[neighbour] = check_val

    return area


def get_area_cost(area):
    size = len(area)
    sides = {
        Direction.N: [],
        Direction.E: [],
        Direction.S: [],
        Direction.W: []
    }

    # Create a dict of relative directions for missing neighbours
    for to_check in area:
        for neighbour in [to_check + one_step(d) for d in [Direction.N, Direction.S, Direction.E, Direction.W]]:
            if not is_in_grid(neighbour, area):
                sides[get_one_step_direction(to_check, neighbour)].append(neighbour)

    side_count = 0
    for side in sides:
        for miss in sides[side]:
            # Missing neighbours on N/S form a line in E/W direction
            if side == Direction.N or side == Direction.S:
                if miss + one_step(Direction.E) not in sides[side]:
                    side_count += 1

            # Missing neighbours on E/W form a line in N/S direction
            if side == Direction.E or side == Direction.W:
                if miss + one_step(Direction.N) not in sides[side]:
                    side_count += 1

    return side_count * size


def process(lines):
    grid = get_grid(lines)

    total = 0
    while grid:
        # Get any point from the grid
        to_check = next(iter(grid))

        # Get area the point belongs to
        area = get_area(to_check, grid)
        total += get_area_cost(area)

        # Remove the area from the grid
        # to avoid checking it multiple times
        grid = {k: v for k, v in grid.items() if k not in area}

    return total


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))
