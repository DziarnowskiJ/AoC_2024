from utils.geometry import *
import re
import platform

base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_14.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_14.txt', 'r') as file:
    sample_lines = [i.rstrip("\n") for i in file.readlines()]


class Robot:
    def __init__(self, pX, pY, vX, vY):
        self.point = Point(pX, pY)
        self.vel = Point(vX, vY)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"Robot p={self.point}, v={self.vel}"


def get_grid(lines, ne, sw):
    grid = empty_grid(ne, sw)

    robots = dict()
    for i, line in enumerate(lines):
        pX, pY, vX, vY = [int(i) for i in re.findall(r"-?\d+", line)]
        robots[i] = Robot(pX, -pY, vX, -vY)

    return grid, robots


def move_robot(robot, grid_bounds, times):
    new_point = robot.point + robot.vel.mul(times)
    new_point = Point(new_point.x % (grid_bounds[1].x + 1), (new_point.y % (grid_bounds[1].y - 1)))

    robot.point = new_point

def process(lines, ne, sw):
    grid, robots = get_grid(lines, ne, sw)
    grid_bounds = (ne, sw)

    for robot_id, robot in robots.items():
        move_robot(robot, grid_bounds, 100)

    quad = {
        'ne': 0,
        'nw': 0,
        'sw': 0,
        'se': 0,
    }

    midpoint = sw.mul(0.5)
    for robot_id, robot in robots.items():
        point = robot.point
        if point.x > midpoint.x and point.y > midpoint.y:
            quad['nw'] += 1
        elif point.x > midpoint.x and point.y < midpoint.y:
            quad['sw'] += 1
        elif point.x < midpoint.x and point.y > midpoint.y:
            quad['ne'] += 1
        elif point.x < midpoint.x and point.y < midpoint.y:
            quad['se'] += 1

    total = quad['nw'] * quad['sw'] * quad['ne'] * quad['se']
    return total




print("Sample output:", process(sample_lines, origin, Point(10, -6)))
print("Answer:", process(input_lines, origin, Point(100, -102)))
