import re

with open('../inputs/real/input_day_3.txt', 'r') as file:
    lines = [i.rstrip("\n") for i in file.readlines()]

with open('../inputs/sample/sample_input_day_3.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def extract_tokens(lines):
    token_regex = (r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)")
    vals = [re.findall(token_regex, line) for line in lines]
    tokens = [item for sublist in vals for item in sublist]
    return tokens


def get_enabled_muls(tokens):
    enabled = True
    enabled_muls = []
    for i in tokens:
        if i == "don't()":
            enabled = False
        elif i == "do()":
            enabled = True
        elif enabled:
            enabled_muls.append(re.findall(r"\d+", i))
    return enabled_muls


def process(line):
    all_tokens = extract_tokens(line)
    enabled_muls = get_enabled_muls(all_tokens)
    mul_results = [int(m[0]) * int(m[1]) for m in enabled_muls]
    return sum(mul_results)


print("Sample output:", process(sample_lines))
print("Answer:", process(lines))
