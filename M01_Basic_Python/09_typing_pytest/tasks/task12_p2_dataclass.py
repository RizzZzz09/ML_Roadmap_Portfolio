from dataclasses import dataclass


@dataclass(frozen=True)
class P2:
    x: int
    y: int


def translate(ps: list[P2], dx: int, dy: int) -> list[P2]:
    return [P2(p.x + dx, p.y + dy) for p in ps]


def main() -> None:
    points = [P2(0, 0), P2(2, 2)]
    dx = 1
    dy = -1
    print(translate(points, dx, dy))


if __name__ == "__main__":
    main()
