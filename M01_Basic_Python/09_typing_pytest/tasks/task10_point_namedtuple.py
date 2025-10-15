from math import hypot
from typing import NamedTuple


class Point(NamedTuple):
    x: float
    y: float


def distance(first_point: Point, second_point: Point) -> float:
    dx = first_point[0] - second_point[0]
    dy = first_point[1] - second_point[1]
    return hypot(dx, dy)


def main() -> None:
    a = Point(0, 0)
    b = Point(3, 4)
    print(distance(a, b))


if __name__ == "__main__":
    main()
