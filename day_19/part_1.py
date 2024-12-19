import platform
import re
from functools import cache

base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_19.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_19.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def parse_input(lines):
    patterns = lines[0].split(', ')
    designs = lines[2:]
    return patterns, designs


def process(lines):
    patterns, designs = parse_input(lines)

    # OPTION 1
    regex = r'(' + '|'.join(patterns) + ')+'
    return sum([bool(re.fullmatch(regex, line)) for line in designs])

    # OPTIONS 2
    # @cache
    # def match(des):
    #     return 1 if des == '' else any(match(des[len(pat):]) for pat in patterns if des.startswith(pat))
    # return sum(match(des) for des in designs)


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))
