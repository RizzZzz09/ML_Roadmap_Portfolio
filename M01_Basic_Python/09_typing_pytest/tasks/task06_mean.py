from typing import List


def mean(numbers: List[int | float]) -> float | None:
    if numbers:
        return sum(numbers) / len(numbers)
    return None


def main() -> None:
    result = mean([1, 2, 3, 4, 5, 5.0])
    print(result)

    result = mean([])
    print(result)


if __name__ == "__main__":
    main()
