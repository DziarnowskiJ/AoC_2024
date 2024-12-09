with open('../inputs/real/input_day_9.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open('../inputs/sample/sample_input_day_9.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def split_input(line):
    files = list()
    free = list()
    for i in range(len(line)):
        if i % 2 == 0:
            files.append(int(line[i]))
        else:
            free.append(int(line[i]))
    return files, free


def unpack_files(files, free):
    unpacked_files = list()
    for i in range(len(files)):
        unpacked_files += [i] * files[i]
        if i < len(free):
            unpacked_files += ['#'] * free[i]
    return unpacked_files


def swap(i, j, files):
    temp = files[i]
    files[i] = files[j]
    files[j] = temp
    return files


def find_non_empty(line):
    for i in range(len(line) - 1, -1, -1):
        if line[i] != '#':
            return i
    return -1


def fix_list(files):
    for i in range(len(files)):
        if files[i] == '#':
            non_empty = find_non_empty(files)
            if non_empty > 0 and non_empty > i:
                files = swap(i, non_empty, files)
    return files


# def fix_list(files):
#     rev = files[::-1]
#     for i in range(len(files)):
#         if files[i] == '#':
#             non_empty = find_non_empty(files)
#             if non_empty > 0 and non_empty > i:
#                 files[i] = rev.pop(0)
#     return files

def get_checksum(files):
    checksum = 0
    for i in range(len(files)):
        if files[i] == '#':
            return checksum
        checksum += i * files[i]
    return checksum


def process(lines):
    files, free = split_input(lines[0])
    unpacked = unpack_files(files, free)
    ordered = fix_list(unpacked)
    checksum = get_checksum(unpacked)
    return checksum


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))
