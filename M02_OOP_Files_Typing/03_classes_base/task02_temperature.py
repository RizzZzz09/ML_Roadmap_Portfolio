from typing import Literal, Union


class InvalidValue(Exception):
    """Ошибка. Выбрасывается если значение температуры не число."""

    pass


class InvalidScale(Exception):
    """Ошибка. Выбрасывается если некорректно введена единица измерения."""

    pass


class Temperature:
    def __init__(self, value: Union[int, float], scale: Literal["C", "F"]):
        if not isinstance(value, (int, float)):
            raise InvalidValue(
                f'Текущее значение температуры: "{value}" некорректно. '
                f"Допустимые значения: только числа."
            )

        if scale not in ("C", "F"):
            raise InvalidScale(f'Неизвестная единица измерения температуры "{scale}".')

        self._value: Union[int, float] = value
        self._scale: Literal["C", "F"] = scale

    @property
    def value(self) -> Union[int, float]:
        return self._value

    @value.setter
    def value(self, value: Union[int, float]) -> None:
        if not isinstance(value, (int, float)):
            raise InvalidValue(
                f'Текущее значение температуры: "{value}" некорректно. '
                f"Допустимые значения: только числа."
            )
        self._value = value

    @property
    def scale(self) -> str:
        return self._scale

    @property
    def celsius(self) -> Union[int, float]:
        if self.scale == "C":
            return self.value
        else:
            return round((self.value - 32) * 5 / 9, 2)

    def __repr__(self) -> str:
        return f"Temperature(value={self.value}, scale={self.scale!r})"

    def __str__(self) -> str:
        return f"{self.value}°{self.scale}"


def main() -> None:
    value = 20

    try:
        temperature = Temperature(value, "F")
    except InvalidScale as error:
        print(f"> {error}")
    else:
        print(temperature.celsius)
        print(temperature)
        print(repr(temperature))


if __name__ == "__main__":
    main()
