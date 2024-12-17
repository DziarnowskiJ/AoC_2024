import heapq
from utils.geometry import *
import platform

base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_16.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_16.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def get_grid(lines):
    grid = grid_dict('\n'.join(lines))
    return {k: v for k, v in grid.items() if v != '#'}


def get_options(cur, grid):
    yield 1000, (cur[0], turn_left(cur[1]))
    yield 1000, (cur[0], turn_right(cur[1]))
    if is_in_grid(cur[0] + one_step(cur[1]), grid):
        yield 1, (cur[0] + one_step(cur[1]), cur[1])


def dijkstra(start, goal, grid):
    priority_queue = [(0, start, [None, start])]
    visited = dict()

    while priority_queue:
        current_distance, current, path = heapq.heappop(priority_queue)

        if current[0] == goal:
            return path, visited, current_distance

        if current in visited:
            dis = visited[current][0][0]
            if dis > current_distance:
                visited[current] = [(current_distance, path[-2])]
            elif dis == current_distance:
                visited[current].append((current_distance, path[-2]))
            continue
        else:
            visited[current] = [(current_distance, path[-2])]

        for distance, neighbor in get_options(current, grid):
            if neighbor not in visited:
                new_distance = current_distance + distance
                heapq.heappush(priority_queue, (new_distance, neighbor, path + [neighbor]))

    return [], visited


def process(lines):
    grid = get_grid(lines)
    start = grid_position('S', grid)[0]
    end = grid_position('E', grid)[0]
    path, visited, distance = dijkstra((start, Direction.E), end, grid)

    reversed_path = path[-2:1:-1]
    nodes = set()
    while reversed_path:
        point = reversed_path.pop(0)
        if point != (start, Direction.E):
            options = [p[1] for p in visited[point] if p[1] not in nodes]
            nodes.update({option for option in options})
            reversed_path += options

    return len({p[0] for p in nodes}) + 2


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))
