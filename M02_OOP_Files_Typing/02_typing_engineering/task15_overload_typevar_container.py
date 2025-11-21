from typing import TypeVar, Union, overload

T = TypeVar("T")


@overload
def wrap(value: list[T]) -> list[T]: ...


@overload
def wrap(value: T) -> list[T]: ...


def wrap(value: Union[T, list[T]]) -> list[T]:
    if isinstance(value, list):
        return value
    else:
        return [value]


def main() -> None:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    result = wrap(numbers)
    print(result)


if __name__ == "__main__":
    main()
