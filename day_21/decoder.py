dirs = {
    '^': {'>': 'A', 'v': 'v'},
    'A': {'v': '>', '<': '^'},
    '<': {'>': 'v'},
    'v': {'^': '^', '>': '>', '<': '<'},
    '>': {'^': 'A', '<': 'v'},
}

nums = {
    'A': {'^': '3', '<': '0'},
    '0': {'^': '2', '>': 'A'},
    '1': {'^': '4', '>': '2'},
    '2': {'^': '5', '>': '3', 'v': '0', '<': '1'},
    '3': {'^': '6', 'v': 'A', '<': '2'},
    '4': {'^': '7', '>': '5', 'v': '1'},
    '5': {'^': '8', '>': '6', 'v': '2', '<': '4'},
    '6': {'^': '9', 'v': '3', '<': '5'},
    '7': {'>': '8', 'v': '4'},
    '8': {'>': '9', 'v': '5', '<': '7'},
    '9': {'v': '6', '<': '8'}
}


def decode(clicks, robot_count):
    pad = dirs if robot_count > 1 else nums

    pos = 'A'
    final = []
    for p in clicks:
        if p == 'A':
            final.append(pos)
        else:
            pos = pad[pos][p]
    if robot_count == 1:
        return ''.join(final)
    # print(''.join(final))  # uncomment to show intermediate steps
    return decode(final, robot_count - 1)


clicks = '<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A'
robot_count = 3
print(decode(clicks, robot_count))
