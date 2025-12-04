from dataclasses import dataclass


@dataclass(order=True)
class Score:
    points: int


def main() -> None:
    print(Score(20) > Score(10))
    print(Score(20) >= Score(20))
    print(Score(10) <= Score(20))


if __name__ == "__main__":
    main()
