import math
from collections import namedtuple


def main():
    Point = namedtuple("Point", ["x", "y"])

    p1 = Point(10, 10)
    p2 = Point(4, 8)

    distance = round(math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2), 4)
    print(f"Distance: {distance}")


if __name__ == "__main__":
    main()
