from typing import Union


class InvalidWidth(Exception):
    """Ошибка. Выбрасывается, если значение ширины отрицательное число или не является числом."""


class InvalidHeight(Exception):
    """Ошибка. Выбрасывается, если значение длины отрицательное число или не является числом."""


class Shape:
    def area(self) -> Union[int, float]:
        return 0

    def perimeter(self) -> Union[int, float]:
        return 0


class Rectangle(Shape):
    def __init__(self, width: Union[int, float], height: Union[int, float]):
        if not isinstance(width, (int, float)) or width <= 0:
            raise InvalidWidth(
                f"Значение ширины может быть только положительным числом. Invalid width={width}"
            )

        if not isinstance(height, (int, float)) or height <= 0:
            raise InvalidHeight(
                f"Значение длины может быть только положительным числом. Invalid height={height}"
            )

        self._width = width
        self._height = height

    @property
    def width(self) -> Union[int, float]:
        return self._width

    @property
    def height(self) -> Union[int, float]:
        return self._height

    def area(self) -> Union[int, float]:
        return self.width * self.height

    def perimeter(self) -> Union[int, float]:
        return 2 * (self.width + self.height)


def main() -> None:
    width = 20
    height = 10

    try:
        rectangle = Rectangle(width, height)
    except (InvalidWidth, InvalidHeight) as error:
        print(f"> {error}")
    else:
        print(rectangle.area())
        print(rectangle.perimeter())


if __name__ == "__main__":
    main()
