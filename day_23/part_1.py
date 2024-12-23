from collections import defaultdict
import platform

base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_23.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_23.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def parse_input(lines):
    conns = defaultdict(list)
    for line in lines:
        k, v = line.split('-')
        conns[k].append(v)
        conns[v].append(k)
    return conns


def process(lines):
    conns = parse_input(lines)

    parties = set()
    for x in conns.keys():
        for y in conns[x]:
            for z in conns[y]:
                if z in conns[x]:
                    parties.add(tuple(sorted(list({x, y, z}))))

    t_keys = {k for k in conns.keys() if k.startswith('t')}
    t_parties = {x for x in parties if any([y in t_keys for y in x])}

    return len(t_parties)


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))
