import tokenize
from io import BytesIO

import pandas as pd
from functools import reduce

with open('../inputs/real/input_day_2.txt', 'r') as file:
    lines = [i.rstrip("\n") for i in file.readlines()]

with open('../inputs/sample/sample_input_day_2.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def prep_line(line):
    vals = [int(item) for item in line.split()]
    sub_lines = []
    for i in range(len(vals)):
        line_copy = vals.copy()
        line_copy.pop(i)
        sub_lines.append(line_copy)
    return sub_lines


def check_line(vals):
    asc = vals[0] < vals[1]
    if vals[0] == vals[1]:
        return False
    for i in range(len(vals) - 1):
        if asc:
            if -3 <= vals[i] - vals[i+1] <= -1:
                continue
            else:
                return False
        else:
            if 3 >= vals[i] - vals[i + 1] >= 1:
                continue
            else:
                return False
    return True


def ans(lines):
    val = 0
    for line in lines:
        if any([check_line(sub_line) for sub_line in prep_line(line)]):
            val += 1
    return val


def process(row):
    return ans(row)


print("Sample output:", process(sample_lines))
print("Answer:", process(lines))
