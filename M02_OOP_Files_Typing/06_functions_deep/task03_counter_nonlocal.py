from typing import Callable


def make_counter() -> Callable[[], int]:
    count_value = 0

    def count() -> int:
        nonlocal count_value
        count_value += 1
        return count_value

    return count


def main() -> None:
    counter = make_counter()
    print(counter())
    print(counter())
    print(counter())
    print(counter())
    print(counter())
    print(counter())


if __name__ == "__main__":
    main()
