with open('../inputs/real/input_day_2.txt', 'r') as file:
    lines = [i.rstrip("\n") for i in file.readlines()]

with open('../inputs/sample/sample_input_day_2.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def check_line(line):
    vals = [int(item) for item in line.split()]
    asc = vals[0] < vals[1]
    if vals[0] == vals[1]:
        return False
    for i in range(len(vals) - 1):
        if asc:
            if -3 <= vals[i] - vals[i+1] <= -1:
                continue
            else:
                return False
        else:
            if 3 >= vals[i] - vals[i + 1] >= 1:
                continue
            else:
                return False
    return True


def ans(lines):
    val = 0
    for line in lines:
        if check_line(line):
            val += 1
    return val


def process(row):
    return ans(row)


print("Sample output:", process(sample_lines))
print("Answer:", process(lines))

