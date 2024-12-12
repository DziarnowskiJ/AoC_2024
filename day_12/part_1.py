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
    perimeter = 0
    for i in area:
        perimeter += 4 - len(get_neighbours(i, area, False))

    return size * perimeter


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
