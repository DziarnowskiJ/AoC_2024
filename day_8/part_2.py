from utils.geometry import *

with open('../inputs/real/input_day_8.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open('../inputs/sample/sample_input_day_8_2.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def get_grid(lines):
    grid = grid_dict('\n'.join(lines))
    return grid


def process(lines):
    grid = get_grid(lines)
    # Distinct frequencies
    freqs = {grid[i] for i in grid.keys() if grid[i] != '.'}
    # Position of antinodes
    antinodes = set()

    for freq in freqs:
        # Get position of all nodes with specific frequency
        nodes = grid_position(freq, grid)

        while nodes:
            # Take first node
            node = nodes.pop(0)

            # Find differences between node and remaining nodes
            node_diffs = {(node - x).mul(-1) for x in nodes}

            # Antinodes could be added straight to antinodes set but this helps in debug
            node_antinodes = set()

            # Find antinodes
            for node_diff in node_diffs:
                # Rising - get all antinodes in grid that happen because of adding difference
                counter = 0
                while is_in_grid(node + node_diff.mul(counter), grid):
                    node_antinodes.add(node + node_diff.mul(counter))
                    counter += 1

                # Falling - get all antinodes in grid that happen because of subtracting difference
                counter = 0
                while is_in_grid(node - node_diff.mul(counter), grid):
                    node_antinodes.add(node - node_diff.mul(counter))
                    counter += 1

            # Update antinodes
            antinodes.update(node_antinodes)

    return len(antinodes)


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))
