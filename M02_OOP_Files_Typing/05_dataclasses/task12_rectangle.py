from dataclasses import dataclass, field
from typing import Union


@dataclass
class Rectangle:
    width: Union[int, float]
    height: Union[int, float]
    area: Union[int, float] = field(init=False)

    def __post_init__(self) -> None:
        self.area = self.width * self.height


def main() -> None:
    rectangle = Rectangle(10, 7)
    print(rectangle)


if __name__ == "__main__":
    main()
