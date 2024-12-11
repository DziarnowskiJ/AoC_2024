import re
import platform
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_11.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_11_2.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]
  

def process_stone(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        half_length = len(stone_str) // 2
        return [int(stone_str[:half_length]), int(stone_str[half_length:])]
    else:
        return [stone * 2024]

def blink(stones):
    after_blink = list()
    for stone in stones:
        after_blink += process_stone(stone)
    return after_blink
    
def process(lines):
    after_blink = [int(i) for i in re.findall(r"\d+", lines[0])]
    # print(after_blink)
    for i in range(25):
        after_blink = blink(after_blink)
        # print(i, '-->', after_blink)
    return len(after_blink)

print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

