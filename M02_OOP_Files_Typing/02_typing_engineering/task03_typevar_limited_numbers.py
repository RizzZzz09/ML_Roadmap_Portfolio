from typing import Sequence, TypeVar

T = TypeVar("T", int, float)


def average(xs: Sequence[T]) -> float:
    return sum(xs) / len(xs)


def main() -> None:
    number_list = [1, 2.5, 3]
    result = average(number_list)
    print(result)


if __name__ == "__main__":
    main()
