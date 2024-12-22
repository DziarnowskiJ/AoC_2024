import platform
from collections import deque

base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_22.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_22_2.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def add_dicts(dicts):
    result = {}
    all_keys = set()
    for d in dicts:
        all_keys.update(d.keys())

    for key in all_keys:
        result[key] = sum(d.get(key, 0) for d in dicts)

    return result


def get_secret(initial_secret):
    secret = initial_secret

    changes = deque(maxlen=4)
    yield secret % 10, tuple(changes)
    while True:
        new_secret = secret
        step_1 = new_secret * 64
        mix_step_1 = step_1 ^ secret
        prune_step_1 = mix_step_1 % 16777216

        step_2 = prune_step_1 // 32
        mix_step_2 = step_2 ^ prune_step_1
        prune_step_2 = mix_step_2 % 16777216

        step_3 = prune_step_2 * 2048
        mix_step_3 = step_3 ^ prune_step_2
        prune_step_3 = mix_step_3 % 16777216

        cost = prune_step_3 % 10
        last_cost = secret % 10
        changes.append(cost - last_cost)
        yield cost, tuple(changes)
        secret = prune_step_3


def process(lines):
    all_dicts = []
    for line in lines:
        secret_gen = get_secret(int(line))
        costs_dict = dict()
        next(secret_gen)
        for _ in range(2000):
            cost, changes = next(secret_gen)
            if changes not in costs_dict and len(changes) == 4:
                costs_dict[changes] = cost
        all_dicts.append(costs_dict)
    full_dict = add_dicts(all_dicts)

    max_cost = 0
    best_seq = None
    for key, val in full_dict.items():
        if max_cost < val:
            max_cost = val
            best_seq = key
    return full_dict[best_seq]


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))
