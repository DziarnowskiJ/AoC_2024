from enum import IntEnum
from typing_extensions import Self


###################################################### DIRECTIONS ######################################################

# compass points
class Direction(IntEnum):
    N = 0
    NE = 1
    E = 2
    SE = 3
    S = 4
    SW = 5
    W = 6
    NW = 7

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Direction.{self.name}'


# the direction immediately to the left
def turn_left(direction: Direction) -> Direction:
    return Direction((direction - 2) % 8)


# the direction immediately to the right
def turn_right(direction: Direction) -> Direction:
    return Direction((direction + 2) % 8)


# Opposite direction
def get_opposite_direction(direction: Direction) -> Direction:
    return Direction((direction + 4) % 8)


######################################################## POINT #########################################################


# x and y coordinates in two-dimensional space
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.key = (x, y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: Self):
        return not self.__eq__(other)

    def __lt__(self, other: Self):
        return (self.x, self.y) < (other.x, other.y)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __sub__(self, other: Self) -> Self:
        return Point(self.x - other.x, self.y - other.y)

    def __add__(self, other: Self) -> Self:
        return Point(self.x + other.x, self.y + other.y)

    def __hash__(self):
        return hash(self.key)

    # multiply both components of a point by a given number
    def mul(self, n: int) -> Self:
        return Point(n * self.x, n * self.y)

    # Manhattan metric of the point
    def norm(self) -> int:
        return abs(self.x) + abs(self.y)


# the origin of the two-dimensional space
origin = Point(0, 0)


# distance between two points using the Manhattan metric
def distance(p1: Point, p2: Point) -> int:
    return (p1 - p2).norm()


# the point one unit from the origin in the given direction
def one_step(direction: Direction) -> Point:
    steps = {
        Direction.N: Point(0, 1),
        Direction.NE: Point(1, 1),
        Direction.E: Point(1, 0),
        Direction.SE: Point(1, -1),
        Direction.S: Point(0, -1),
        Direction.SW: Point(-1, -1),
        Direction.W: Point(-1, 0),
        Direction.NW: Point(-1, 1),
    }
    return steps[direction]


def get_one_step_direction(point1: Point, point2: Point) -> Direction | None:
    diff = point2 - point1

    direction_map = {
        (0, 1): Direction.N,
        (1, 1): Direction.NE,
        (1, 0): Direction.E,
        (1, -1): Direction.SE,
        (0, -1): Direction.S,
        (-1, -1): Direction.SW,
        (-1, 0): Direction.W,
        (-1, 1): Direction.NW
    }

    return direction_map.get(diff.key)


def point_neighbours(point: Point, diagonal: bool = True) -> list[Point]:
    return [point + one_step(Direction(i)) for i in Direction if diagonal or i % 2 == 0]


######################################################### GRID #########################################################

def grid_dict(text_grid: str, origin: Direction = Direction.NE) -> dict[Point, str]:
    lines_of_text = text_grid.split('\n')
    if origin == Direction.NE:
        return {Point(x, -y): c for y, line in enumerate(lines_of_text)
                for x, c in enumerate(line)}
    elif origin == Direction.NW:
        return {Point(-x, -y): c for y, line in enumerate(lines_of_text)
                for x, c in enumerate(reversed(line))}
    elif origin == Direction.SE:
        return {Point(x, y - 1): c for y, line in enumerate(reversed(lines_of_text))
                for x, c in enumerate(line)}
    elif origin == Direction.SW:
        return {Point(-x, y - 1): c for y, line in enumerate(reversed(lines_of_text))
                for x, c in enumerate(reversed(line))}
    else:
        raise Exception("origin can only be NE, NW, SE or SW")


def get_neighbours_dict(point: Point, grid: dict[Point, str],
                        diagonal: bool = True) -> dict[Point, str]:
    return {p: grid[p] for p in point_neighbours(point, diagonal) if is_in_grid(p, grid)}


def get_neighbours_values(point: Point, grid: dict[Point, str],
                          diagonal: bool = True) -> list[str]:
    return [v for v in get_neighbours_dict(point, grid, diagonal).values()]


def is_in_grid(point: Point, grid: dict[Point, str]) -> bool:
    return point in grid.keys()


def grid_dimensions(grid: dict[Point, str]) -> tuple[Point, Point]:
    xs = [p.x for p in grid.keys()]
    ys = [p.y for p in grid.keys()]

    top_left = Point(min(xs), max(ys))
    bottom_right = Point(max(xs), min(ys))

    return top_left, bottom_right


def grid_position(char: str, grid: dict[Point, str]) -> list[Point]:
    return [key for key, value in grid.items() if value == char]


def points_to_text(grid: dict[Point, str]) -> str:
    # Find the maximum and minimum coordinates to determine the size of the grid
    g_bounds = grid_dimensions(grid)
    max_x = g_bounds[1].x
    min_x = g_bounds[0].x
    max_y = g_bounds[0].y
    min_y = g_bounds[1].y

    # Initialize an empty grid with spaces
    text_grid = [[' ' for _ in range(abs(max_x - min_x) + 1)] for _ in range(abs(max_y - min_y) + 1)]

    # Populate the grid with characters from the given points
    for point, char in grid.items():
        x = abs(max_x - min_x) - abs(point.x - max_x)
        y = abs(max_y - min_y) - abs(point.y - max_y)
        text_grid[y][x] = char

    # Convert the grid to a string
    text = '\n'.join(''.join(row) for row in reversed(text_grid))

    return text


def empty_grid(nw_point: Point, se_point: Point, char: str = '.') -> dict[Point, str]:
    grid = dict()
    for i in range(nw_point.x, se_point.x + 1, 1):
        for j in range(nw_point.y, se_point.y - 1, -1):
            grid[Point(i, j)] = char
    return grid
