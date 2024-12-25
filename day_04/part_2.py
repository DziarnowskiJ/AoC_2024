from utils.geometry import *

with open('../inputs/real/input_day_4.txt', 'r') as file:
    lines = [i.rstrip("\n") for i in file.readlines()]

with open('../inputs/sample/sample_input_day_4_2.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def process(lines):
    grid = grid_dict('\n'.join(lines))
    starts = grid_position('A', grid)
    counter = 0
    for x in starts:
        # Get only diagonal neighbours of A that are M
        neighbours_a = [get_one_step_direction(x, neigh) for neigh in get_neighbours_dict(x, grid, True) if
                        grid[neigh] == 'M' and neigh not in [n for n in get_neighbours_dict(x, grid, False)]]
        # If there aren't 2 neighbours, shape can't be made
        if len(neighbours_a) != 2:
            continue
        # For both, check if in the opposite direction of A->M is S
        if all([(is_in_grid(x + one_step(get_opposite_direction(m)), grid)
                 and grid[x + one_step(get_opposite_direction(m))] == 'S') for m in neighbours_a]):
            counter += 1
    return counter


print("Sample output:", process(sample_lines))
print("Answer:", process(lines))
