from typing import Literal, overload


class ConversionErrorForInt(Exception):
    """Ошибка. Выбрасывается, если не удалось привести значение к int."""

    pass


class ConversionErrorForFloat(Exception):
    """Ошибка. Выбрасывается, если не удалось привести значение к float."""

    pass


class InvalidMode(Exception):
    """Ошибка. Выбрасывается, если введен некорректный режим работы."""

    pass


@overload
def parse_data(raw: str, mode: Literal["int"]) -> int: ...


@overload
def parse_data(raw: str, mode: Literal["float"]) -> float: ...


@overload
def parse_data(raw: str, mode: Literal["str"]) -> str: ...


def parse_data(raw: str, mode: Literal["int", "float", "str"]) -> int | float | str:
    if mode == "int":
        try:
            return int(raw)
        except ValueError as error:
            raise ConversionErrorForInt(f'Не удалось преобразовать "{raw}" в число.') from error

    elif mode == "float":
        try:
            return float(raw)
        except ValueError as error:
            raise ConversionErrorForFloat(
                f'Не удалось преобразовать "{raw}" в число с плавающей точкой.'
            ) from error

    elif mode == "str":
        return raw
    else:
        raise InvalidMode(f'Данный режим работы "{mode}" не поддерживается программой.')


def main() -> None:
    try:
        result = parse_data("10", "int")
    except (ConversionErrorForInt, ConversionErrorForFloat) as error:
        print(error, f"\n> {error.__cause__}")
    except InvalidMode as error:
        print(f"> {error}")
    else:
        print(result)


if __name__ == "__main__":
    main()
