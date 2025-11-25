from typing import Annotated


class InvalidValue(Exception):
    """Ошибка. Выбрасывается, если число неположительное."""

    pass


class Box:
    def __init__(self, width: Annotated[int, "width>0"], height: Annotated[int, "height>0"]):
        if width <= 0 or height <= 0:
            raise InvalidValue("Атрибуты класса должны быть больше 0.")

        self._width: int = width
        self._height: int = height

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value: Annotated[int, "width>0"]) -> None:
        if value <= 0:
            raise InvalidValue("Ширина не может быть меньше или равной 0.")
        self._width = value

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, value: Annotated[int, "height>0"]) -> None:
        if value <= 0:
            raise InvalidValue("Высота не может быть меньше или равна 0.")
        self._height = value

    @property
    def area(self) -> int:
        return self.width * self.height

    def __repr__(self) -> str:
        return f"Box(width={self.width}, height={self.height})"


def main() -> None:
    width = 20
    height = 10

    try:
        box = Box(width, height)
    except InvalidValue as error:
        print(f"> {error}")
    else:
        print(box.area)
        print(repr(box))


if __name__ == "__main__":
    main()
