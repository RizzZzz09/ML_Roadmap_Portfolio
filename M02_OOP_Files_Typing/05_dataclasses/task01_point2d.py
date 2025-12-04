from dataclasses import dataclass


@dataclass
class Point2D:
    x: int
    y: int


def main() -> None:
    first_point = Point2D(2, 2)
    second_point = Point2D(2, 4)

    print(first_point)
    print(second_point)

    print(first_point == second_point)
    print(first_point == first_point)


if __name__ == "__main__":
    main()
