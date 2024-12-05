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


def get_incorrect_lines(part2, part1):
    incorrect_lines = list()
    for line in part2:
        is_correct = True
        for reg in part1:
            # Preform check if both numbers from the rule are in the list
            if all(item in line for item in reg):
                if line.index(reg[0]) > line.index(reg[1]):
                    is_correct = False
                    break
        # If line is incorrect add it to the list
        if not is_correct:
            incorrect_lines.append(line)
    return incorrect_lines


def fix_line(incorrect_line, part1):
    # Create priority dict
    priority_dict = {k: 0 for k in incorrect_line}
    for rl in part1:
        # If both parts of the rule are in the incorrect_line
        # adjust their priority based on the rules
        if all([r in priority_dict.keys() for r in rl]):
            priority_dict[rl[0]] += 1
            priority_dict[rl[1]] -= 1

    def sort_key(num):
        return priority_dict[num]

    # Sort line based on priority_dict
    return sorted(incorrect_line, key=sort_key)


def process(line):
    part1, part2 = split_input(line)
    incorrect_lines = get_incorrect_lines(part2, part1)
    counter = 0
    for incorrect_line in incorrect_lines:
        fixed_line = fix_line(incorrect_line, part1)
        counter += fixed_line[(len(fixed_line) // 2)]
    return counter


print("Sample output:", process(sample_lines))
print("Answer:", process(lines))
