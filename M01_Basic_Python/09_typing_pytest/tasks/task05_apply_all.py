from typing import Callable, List


def add(a: int, b: int) -> int:
    return a + b


def sub(a: int, b: int) -> int:
    return a - b


def mul(a: int, b: int) -> int:
    return a * b


def apply_all(a: int, b: int, funcs: List[Callable[[int, int], int]]) -> List[int]:
    return [func(a, b) for func in funcs]


def main() -> None:
    print(apply_all(5, 5, [add, sub, mul]))


if __name__ == "__main__":
    main()
