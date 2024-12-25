import re

with open('../inputs/real/input_day_3.txt', 'r') as file:
    lines = [i.rstrip("\n") for i in file.readlines()]

with open('../inputs/sample/sample_input_day_3.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def extract_muls(line):
    mul_regex = (r"mul\(\d{1,3},\d{1,3}\)")
    vals = [re.findall(mul_regex, l) for l in line]
    muls = [item for sublist in vals for item in sublist]
    return muls


def process(line):
    muls = extract_muls(line)
    all_mul_pairs = [re.findall(r"\d+", mul) for mul in muls]
    mul_results = [int(m[0]) * int(m[1]) for m in all_mul_pairs]
    return sum(mul_results)


print("Sample output:", process(sample_lines))
print("Answer:", process(lines))
