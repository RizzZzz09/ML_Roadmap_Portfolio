from typing import Generic, Iterator, TypeVar

T = TypeVar("T")


class IterableLog(Generic[T]):
    def __init__(self, iterable_list: list[T]) -> None:
        self._iterable_list = iterable_list

    def __len__(self) -> int:
        return len(self._iterable_list)

    def __iter__(self) -> Iterator[T]:
        return iter(self._iterable_list)


def main() -> None:
    data = ["first", "second", "third", "fourth", "fifth"]

    iter_log = IterableLog(data)

    for index, item in enumerate(iter_log):
        if index == 0:
            print(f"{index}. {item} -> Добавлен первым")
        elif index == len(iter_log) - 1:
            print(f"{index}. {item} -> Добавлен последним")
        else:
            print(f"{index}. {item}")


if __name__ == "__main__":
    main()
