from typing import Callable


def make_order(n: int) -> Callable[[int], int]:
    def add(x: int) -> int:
        return x + n

    return add


def main() -> None:
    add5 = make_order(5)

    result = add5(10)
    print(result)


if __name__ == "__main__":
    main()
