from typing import Callable, List, TypeVar

T = TypeVar("T")
U = TypeVar("U")


def map_strict(xs: List[T], func: Callable[[T], U]) -> List[U]:
    return [func(elem) for elem in xs]


def main() -> None:
    print(map_strict([1, 2, 3], lambda x: x * 2))


if __name__ == "__main__":
    main()
