from typing import TypeVar

T = TypeVar("T")


class Box:
    def __init__(self, elements: list[T]) -> None:
        self._elements = elements

    def __len__(self) -> int:
        return len(self._elements)


def main() -> None:
    box = Box(["car", 1, True, "Danil", 1.233])
    print(f"len={len(box)}")


if __name__ == "__main__":
    main()
