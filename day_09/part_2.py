import platform
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_9.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_9.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def unpack_disk(line):
    files = dict()
    disk = dict()
    index = 0
    disk_location = 0
    for digit in [int(digit) for digit in line]:
        if index % 2 == 0:
            files[index // 2] = (disk_location, digit)
            disk.update({disk_location + i: index // 2 for i in range(digit)})
        index += 1
        disk_location += int(digit)

    return files, disk


def compact_disk(files, disk):
    c_disk = disk.copy()
    # Process files from the end to start
    files_to_compact = list(range(max(list(files.keys())), -1, -1))
    for file_id in files_to_compact:
        index = 0

        # Ensure file is inserted to earlier index then their start position
        while index < files[file_id][0]:

            # Check if there's space for file
            if not any(index + i in c_disk for i in range(files[file_id][1])):
                for i in range(files[file_id][1]):
                    del c_disk[files[file_id][0] + i]
                    c_disk[index + i] = file_id
                break
            else:
                index += 1

    return c_disk


def check_sum(disk):
    total = 0
    for loc, file_id in disk.items():
        total += loc * file_id
    return total


def process(lines):
    files, disk = unpack_disk(lines[0])
    compacted_disk = compact_disk(files, disk)
    return check_sum(compacted_disk)


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))
