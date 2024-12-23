from collections import defaultdict
import platform

base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_23.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_23.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def parse_input(lines):
    conns = defaultdict(set)
    links = list()
    for line in lines:
        k, v = line.split('-')
        conns[k].add(v)
        conns[v].add(k)

        for link in conns[k]:
            if link in conns[v]:
                links.append((link, k, v))
    return conns, links


def get_party(subparty, conns):
    new_party = subparty.copy()
    node = new_party[0]
    for conn in conns[node]:
        for check in subparty:
            if conn not in conns[check]:
                break
        else:
            new_party.append(conn)
            break
    if len(new_party) > len(subparty):
        return get_party(new_party, conns)
    return new_party


def process(lines):
    conns, links = parse_input(lines)

    reviewed = set()
    largest_party = None
    for grouping in links:
        if grouping[0] in reviewed:
            continue
        party = get_party(list(grouping), conns)
        for host in party:
            reviewed.add(host)
        if largest_party is None or len(largest_party) < len(party):
            largest_party = party
    largest_party.sort()

    return ','.join(largest_party)


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))
