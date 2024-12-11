import re
import platform

base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_11.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_11_2.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def process_stone(stone):
    stone_str = str(stone)
    length = len(stone_str)

    if stone == 0:
        return [1]
    elif length % 2 == 0:
        half_length = length // 2
        return [int(stone_str[:half_length]),
                int(stone_str[half_length:])]
    else:
        return [stone * 2024]


def blink(stones_dict):
    blink_dict = dict()
    for stone, counts in stones_dict.items():
        new_stones = process_stone(stone)

        # Instead of having list of all stones, have dict with number or same stones
        for new_stone in new_stones:
            if new_stone in blink_dict:
                blink_dict[new_stone] += counts
            else:
                blink_dict[new_stone] = counts
    return blink_dict


def process(lines):
    stones = [int(i) for i in re.findall(r"\d+", lines[0])]
    stones_dict = {i: stones.count(i) for i in stones}
    for _ in range(75):
        stones_dict = blink(stones_dict)

    return sum([v for v in stones_dict.values()])


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))
