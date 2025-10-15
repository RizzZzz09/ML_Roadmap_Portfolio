from typing import Callable, List, TypeVar

T = TypeVar("T")


def filter_keep(xs: List[T], func: Callable[[T], bool]) -> List[T]:
    return [value for value in xs if func(value)]


def main() -> None:
    result = filter_keep([1, 2, 3, 4], lambda v: v % 2 == 0)
    print(result)

    res = filter_keep(["a", "bb", "ccc"], lambda s: len(s) >= 2)
    print(res)


if __name__ == "__main__":
    main()
