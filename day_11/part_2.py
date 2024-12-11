import re
from functools import cache, lru_cache
import platform

base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_11.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_11_2.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]

@cache
def process_stone(stone):
    stone_str = str(stone)
    length = len(stone_str)

    if stone == 0:
        return (1,)
    elif length % 2 == 0:
        half_length = length // 2
        return (int(stone_str[:half_length]),
                int(stone_str[half_length:]))
    else:
        return (stone * 2024,)


@cache
def blink_X(stones, times):
    if times == 0:
        return len(stones)
    return sum(blink_X(process_stone(s), times - 1) for s in stones)


def process(lines):
    stones = tuple(int(i) for i in re.findall(r"\d+", lines[0]))
    return blink_X(stones, 75)


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))
