from utils.geometry import *

with open('../inputs/real/input_day_8.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open('../inputs/sample/sample_input_day_8.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def get_grid(lines):
    grid = grid_dict('\n'.join(lines))
    return grid


def process(lines):
    grid = get_grid(lines)
    freqs = {grid[i] for i in grid.keys() if grid[i] != '.'}
    antinodes = set()

    for freq in freqs:
        nodes = grid_position(freq, grid)
        for node in nodes:
            node_antinodes = {node - (node - x).mul(-1) for x in nodes if x != node}
            antinodes.update(node_antinodes)

    valid_ampfs = {antinode for antinode in antinodes if is_in_grid(antinode, grid)}
    return len(valid_ampfs)


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))
