from utils.geometry import *
import re
import platform

base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_14.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_14_2.txt', 'r') as file:
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
    grid_bounds = grid_dimensions(grid)

    counter = 0
    while True:
        counter += 1
        for robot_id, robot in robots.items():
            move_robot(robot, grid_bounds, 1)

        image = points_to_text({r.point: '#' for r in robots.values()})
        if len(re.findall(r"#########", image)) > 0:
            print(image)
            break

    return counter


print("Sample output:", process(sample_lines, origin, Point(10, -6)))
print("Answer:", process(input_lines, origin, Point(100, -102)))
