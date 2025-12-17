from __future__ import annotations

from typing import Generic, Iterator, Sequence, TypeVar, overload

T = TypeVar("T")


class WindowView(Generic[T]):
    def __init__(self, sequence: Sequence[T]) -> None:
        self._sequence = sequence

    def __len__(self) -> int:
        return len(self._sequence)

    def __iter__(self) -> Iterator[T]:
        return iter(self._sequence)

    @overload
    def __getitem__(self, index: int) -> T: ...

    @overload
    def __getitem__(self, index: slice) -> WindowView[T]: ...

    def __getitem__(self, index: int | slice) -> T | WindowView[T]:
        if isinstance(index, slice):
            return WindowView(self._sequence[index])
        return self._sequence[index]


def main() -> None:
    random_list = ["Danil", 1, 2.3, True, False, "Alina", None]

    window_view = WindowView(random_list)

    print(f"length: {len(window_view)}")

    for index, item in enumerate(window_view):
        print(f"{index}: {item}")

    print(window_view[0])
    print(window_view[-1])

    slice_window = window_view[5:10]
    for index, item in enumerate(slice_window):
        print(f"{index}: {item}")


if __name__ == "__main__":
    main()
