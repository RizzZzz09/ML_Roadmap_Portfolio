from typing import Annotated, Union


class InvalidSide(Exception):
    """Ошибка. Выбрасывается, если значение стороны прямоугольника меньше или равна 0."""

    pass


class Rectangle:
    def __init__(
        self,
        width: Annotated[Union[int, float], "width > 0"],
        height: Annotated[Union[int, float], "height > 0"],
    ):

        if not isinstance(width, (int, float)) or width <= 0:
            raise InvalidSide(
                f'Значение стороны "width={width}: {type(width).__name__}" '
                f"должно быть числом больше 0."
            )

        if not isinstance(height, (int, float)) or height <= 0:
            raise InvalidSide(
                f'Значение стороны "height={height}: {type(height).__name__}" '
                f"должно быть числом больше 0."
            )

        self._width = width
        self._height = height

    @property
    def width(self) -> Union[int, float]:
        return self._width

    @width.setter
    def width(self, value: Union[int, float]) -> None:
        if not isinstance(value, (int, float)) or value <= 0:
            raise InvalidSide(
                f'Значение стороны "width={value}: {type(value).__name__}" '
                f"должно быть числом больше 0."
            )
        self._width = value

    @property
    def height(self) -> Union[int, float]:
        return self._height

    @height.setter
    def height(self, value: Union[int, float]) -> None:
        if not isinstance(value, (int, float)) or value <= 0:
            raise InvalidSide(
                f'Значение стороны "height={value}: {type(value).__name__}" '
                f"должно быть числом больше 0."
            )
        self._height = value

    @property
    def perimeter(self) -> Union[int, float]:
        return 2 * (self.width + self.height)

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

    def __str__(self) -> str:
        return f"Rectangle: {self.width}x{self.height}"


def main() -> None:
    width = 10
    height = 10

    try:
        rectangle = Rectangle(width, height)
    except InvalidSide as error:
        print(f"> {error}")
    else:
        print(rectangle.perimeter)
        print(rectangle)
        print(repr(rectangle))


if __name__ == "__main__":
    main()
