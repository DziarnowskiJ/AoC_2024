from utils.geometry import *
import platform
import heapq

base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_16.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_16.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def get_grid(lines):
    grid = grid_dict('\n'.join(lines))
    return {k: v for k, v in grid.items() if v != '#'}


def dijkstra(prev, start, goal, grid) -> (list[Point], set[Point]):
    priority_queue = [(0, start, prev, [start])]
    visited = set()

    while priority_queue:
        current_distance, current, prev, path = heapq.heappop(priority_queue)

        if current == goal:
            return path, visited

        if current in visited:
            continue

        visited.add(current)

        neighbors = get_neighbours_dict(current, grid, False)
        for neighbor, value in neighbors.items():
            if neighbor not in visited:
                new_distance = (current_distance + 1 +
                                (1000 * get_one_step_direction(current, neighbor) != get_one_step_direction(prev,
                                                                                                            current)))
                heapq.heappush(priority_queue, (new_distance, neighbor, current, path + [neighbor]))

    # If no path is found
    return [], visited


def count_step(path, direction):
    counter = 0
    start = path.pop(0)
    while path:
        next = path.pop(0)
        if get_one_step_direction(start, next) == direction:
            counter += 1
        else:
            counter += 1001
        direction = get_one_step_direction(start, next)
        start = next
    return counter


def process(lines):
    grid = get_grid(lines)
    start = grid_position('S', grid)[0]
    end = grid_position('E', grid)[0]
    path, visited = dijkstra(start + one_step(Direction.W), start, end, grid)

    for p in path:
        grid[p] = '#'
    return count_step(path, Direction.E)


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))
