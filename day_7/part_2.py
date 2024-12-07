with open('../inputs/real/input_day_7.txt', 'r') as file:
    lines = [i.rstrip("\n") for i in file.readlines()]

with open('../inputs/sample/sample_input_day_7.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def can_evaluate_to(target, val, rest):
    if len(rest) == 0:
        return target == val

    if target < val:
        return False

    left, *right = rest
    return (can_evaluate_to(target, val + left, right)
            or can_evaluate_to(target, val * left, right)
            or can_evaluate_to(target, int(str(val) + str(left)), right))


def process(lines):
    total = 0
    for line in lines:
        target, numbers = line.split(': ')
        target = int(target)
        numbers = [int(num) for num in numbers.split()]
        if can_evaluate_to(target, numbers[0], numbers[1:]):
            total += target
    return total


print("Sample output:", process(sample_lines))
print("Answer:", process(lines))
