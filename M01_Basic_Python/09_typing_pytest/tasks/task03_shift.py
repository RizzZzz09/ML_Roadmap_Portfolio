from typing import List, Tuple


def shift(points: List[Tuple[int, int]], dx: int, dy: int) -> List[Tuple[int, int]]:
    return [(x + dx, y + dy) for x, y in points]


def main() -> None:
    points = [(0, 0), (2, 2)]
    result = shift(points, dx=1, dy=-1)
    print(result)


if __name__ == "__main__":
    main()
