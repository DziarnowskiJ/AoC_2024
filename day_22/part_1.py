import platform

base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_22.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_22.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def get_secret(old_secret):
    step_1 = old_secret * 64
    mix_step_1 = step_1 ^ old_secret
    prune_step_1 = mix_step_1 % 16777216

    step_2 = prune_step_1 // 32
    mix_step_2 = step_2 ^ prune_step_1
    prune_step_2 = mix_step_2 % 16777216

    step_3 = prune_step_2 * 2048
    mix_step_3 = step_3 ^ prune_step_2
    prune_step_3 = mix_step_3 % 16777216

    return prune_step_3


def process(lines):
    total = 0
    for line in lines:
        secret = int(line)
        for _ in range(2000):
            secret = get_secret(secret)
        total += secret
    return total


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))
