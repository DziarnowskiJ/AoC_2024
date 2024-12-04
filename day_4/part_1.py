from utils.geometry import *

with open('../inputs/real/input_day_4.txt', 'r') as file:
    lines = [i.rstrip("\n") for i in file.readlines()]

with open('../inputs/sample/sample_input_day_4.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def process(lines):
    grid = grid_dict('\n'.join(lines))
    starts = grid_position('X', grid)
    counter = 0
    for x in starts:
        # Get all neighbours of X that are M and extract the direction X->M
        neighbours_x = [get_one_step_direction(x, neigh)
                        for neigh in get_neighbours_dict(x, grid, True) if grid[neigh] == 'M']
        for m in neighbours_x:
            if (  # Check if 2 steps in direction X->M is A
                    is_in_grid(x + one_step(m).mul(2), grid)
                    and grid[x + one_step(m).mul(2)] == 'A'
                    # Check if 3 steps in direction X->M is S
                    and is_in_grid(x + one_step(m).mul(3), grid)
                    and grid[x + one_step(m).mul(3)] == 'S'):
                counter += 1
    return counter


print("Sample output:", process(sample_lines))
print("Answer:", process(lines))
