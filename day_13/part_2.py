import re
import platform

base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_13.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_13.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


def parse_lines(lines):
    lines_copy = lines.copy()
    lines_copy.append([''])
    machines = []

    while lines_copy:
        but_a = lines_copy.pop(0)
        but_b = lines_copy.pop(0)
        prize = lines_copy.pop(0)
        _ = lines_copy.pop(0)

        mach = {
            'a': tuple([int(i) for i in re.findall(r"\d+", but_a)]),
            'b': tuple([int(i) for i in re.findall(r"\d+", but_b)]),
            'p': tuple([10000000000000 + int(i) for i in re.findall(r"\d+", prize)])
        }

        machines.append(mach)

    return machines


def solve_AB(machine):
    aX, aY = machine['a']
    bX, bY = machine['b']
    pX, pY = machine['p']
    sA = aX + aY
    sB = bX + bY
    sP = pX + pY

    # Button A: X + aX, Y + aY
    # Button B: X + bX, Y + bY
    # Prize: X = pX, Y = pY

    # aS = aX + aY
    # bS = bX + bY
    # pS = pX + pY

    # pX = A * aX + B * bX                          (1)
    # pY = A * aY + B * bY                          (2)
    # + ______________________
    # pX + pY = A * (aX + aY) + B * (bX + bY)       (1) + (2)  // * bX
    # pS * bX = A * aS * bX + B * bS * bX           (3)

    # pX = A * aX + B * bX                          (1) // * bS
    # pX * bS = A * aX * bS + B * bX * bS           (4)

    # --------------------------------------

    # pX * bS = A * aX * bS + B * bX * bS  (4)
    # pS * bX = A * aS * bX + B * bS * bX  (3)
    # - __________________________
    # pX * bS - pS * bX = A * (aX * bS - aS * bX)   (4) - (3) // / (aX * bS - aS * bX)
    # (pX * bS - pS * bX) / (aX * bS - aS * bX) = A

    # ---------------------------------------

    # pX = A * aX + B * bX                          (1) // - A * aX
    # pX - A * aX = B * bX                          // / bX
    # (pX - A * aX) / bX = B

    A = (pX * sB - sP * bX) / (aX * sB - sA * bX)
    B = (pX - A * aX) / bX

    return A, B


def process(lines):
    machines = parse_lines(lines)

    counter = 0
    for machine in machines:
        A, B = solve_AB(machine)
        if A.is_integer() and B.is_integer():
            counter += A * 3 + B

    return int(counter)


print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))
