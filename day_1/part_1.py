with open('../inputs/real/input_day_1.txt', 'r') as file:
    lines = [i.rstrip("\n") for i in file.readlines()]

with open('../inputs/sample/sample_input_day_1.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def convert(lines):
    locations1 = []
    locations2 = []
    for i in lines:
        words = i.split()
        locations1.append(int(words[0]))
        locations2.append(int(words[1]))

    return locations1, locations2


def calc(locations1, locations2):
    locations1.sort()
    locations2.sort()

    total = 0
    for i in range(len(locations1)):
        total += abs(locations1[i] - locations2[i])

    return total


def process(lines):
    locations1, locations2 = convert(lines)
    return calc(locations1, locations2)


print("Sample output:", process(sample_lines))
print("Answer:", process(lines))

