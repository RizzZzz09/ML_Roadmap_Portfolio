from dataclasses import dataclass
from typing import Literal, Union


class InvalidTemperatureValue(Exception):
    """Ошибка. Выбрасывается если температура не int или float."""

    pass


class InvalidTemperatureUnit(Exception):
    """Ошибка. Выбрасывается если единица измерения температуры не "C" или "F"."""

    pass


@dataclass
class Temperature:
    value: Union[int, float]
    unit: Literal["C", "F"]

    def __post_init__(self) -> None:
        if not isinstance(self.value, (int, float)) or isinstance(self.value, bool):
            raise InvalidTemperatureValue(
                f'Значение: "{self.value}: {type(self.value).__name__}" не поддерживается.'
                f"\n\t- Поддерживающиеся форматы: (int, float)."
            )

        if self.unit not in ("C", "F"):
            raise InvalidTemperatureUnit(
                f'Единица измерения: "{self.unit}" не поддерживается.'
                f'\n\t- Поддерживающиеся единицы измерения: ("C", "F").'
            )


def main() -> None:
    try:
        temperature_now = Temperature(20, "C")
    except (InvalidTemperatureValue, InvalidTemperatureUnit) as error:
        print(f"> {error}")
    else:
        print(temperature_now)


if __name__ == "__main__":
    main()
