import re

with open('../inputs/real/input_day_5.txt', 'r') as file:
    lines = [i.rstrip("\n") for i in file.readlines()]

with open('../inputs/sample/sample_input_day_5.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def split_input(lines):
    empty_list = [i for i in range(len(lines)) if len(lines[i]) == 0][0]
    part1 = [[int(i) for i in re.findall(r"\d+", line)] for line in lines[:empty_list]]
    part2 = [[int(i) for i in re.findall(r"\d+", line)] for line in lines[empty_list + 1:]]
    return part1, part2


def check_line(lines, part1):
    counter = 0
    for line in lines:
        is_correct = True
        for rule in part1:
            # Preform check if both numbers from the rule are in the list
            if all(item in line for item in rule):
                if line.index(rule[0]) > line.index(rule[1]):
                    is_correct = False
                    break
        if is_correct:
            counter += line[(len(line) // 2)]
    return counter


def process(line):
    part1, part2 = split_input(line)
    return check_line(part2, part1)


print("Sample output:", process(sample_lines))
print("Answer:", process(lines))
