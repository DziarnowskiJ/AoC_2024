from utils.geometry import *

with open('../inputs/real/input_day_6.txt', 'r') as file:
    lines = [i.rstrip("\n") for i in file.readlines()]

with open('../inputs/sample/sample_input_day_6_2.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def get_grid(lines):
    return grid_dict('\n'.join(lines))


def process(line):
    grid = get_grid(line)
    guard_pos = grid_position('^', grid)[0]
    grid[guard_pos] = 'X'
    guard_dir = Direction.N
    counter = 1
    guard_steps = dict()
    hit_count = 0
    obs_pos = set()
    hit_dir = dict()
    while is_in_grid(guard_pos + one_step(guard_dir), grid):
        if hit_count >= 3:
            poss_pos = guard_pos + one_step(guard_dir)
            print('guard at ', guard_pos, guard_dir, '-->', poss_pos)
            # If poss_pos is in grid
            if poss_pos.key not in hit_dir.keys():
                while is_in_grid(poss_pos, grid):
                    print('as', poss_pos)
                    if poss_pos == Point(3, -6):
                        print(hit_dir)
                        print('-->', poss_pos - one_step(turn_right(guard_dir)))
                    if grid[poss_pos] == 'X':
                        pass
                    # elif ((poss_pos.key in hit_dir.keys()
                    #        and poss_pos - one_step(turn_right(guard_dir)) in hit_dir[poss_pos.key])):
                    elif ((poss_pos.key in hit_dir.keys()
                           and poss_pos - one_step(turn_right(guard_dir)) in hit_dir[poss_pos.key])):
                        print('-----------------found ', guard_pos + one_step(guard_dir).mul(2))
                        print(hit_dir)
                        obs_pos.add(guard_pos + one_step(guard_dir).mul(2))
                    elif grid[poss_pos] == '#':
                        print('new obs')
                        break
                    poss_pos += one_step(turn_right(guard_dir))

        next_step = guard_pos + one_step(guard_dir)
        if grid[next_step] == '#':
            hit_count += 1
            print('hit---------------------------------')

            if next_step.key in hit_dir.keys():
                hit_dir[next_step.key].append(guard_pos)
            else:
                hit_dir[next_step.key] = [guard_pos]

            guard_dir = Direction((guard_dir + 2) % 8)

        else:
            if grid[guard_pos] != 'X':
                if guard_pos.key in guard_steps.keys():
                    guard_steps[guard_pos.key].append(guard_dir)
                else:
                    guard_steps[guard_pos.key] = [guard_dir]
            grid[guard_pos] = 'X'
            guard_pos = guard_pos + one_step(guard_dir)

    print(obs_pos)
    return len(obs_pos)


print("Sample output:", process(sample_lines))
# print("Answer:", process(lines))

# > 340
