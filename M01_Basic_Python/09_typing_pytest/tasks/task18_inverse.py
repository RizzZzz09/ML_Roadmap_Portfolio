from typing import List


def inverse(numbers: List[float]) -> List[float | None]:
    return [1 / number if number != 0 else None for number in numbers]


def main() -> None:
    print(inverse([1, 2, 4]))
    print(inverse([1, 0, 5, 7]))


if __name__ == "__main__":
    main()
