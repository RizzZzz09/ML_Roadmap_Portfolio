import random
from typing import Iterable, TypeVar

T = TypeVar("T")


def shuffle_list(xs: list[T]) -> list[T]:
    new_list = xs[:]
    random.shuffle(new_list)
    return new_list


def unique(xs: Iterable[T]) -> list[T]:
    list_unique_items = []
    for item in xs:
        if item not in list_unique_items:
            list_unique_items.append(item)
    return list_unique_items


def main() -> None:
    number_list = [number for number in range(10)]
    result = shuffle_list(number_list)
    print(result)

    number_tuple = (5, 5, 5, 1, 2, 1)
    result = unique(number_tuple)
    print(result)


if __name__ == "__main__":
    main()
