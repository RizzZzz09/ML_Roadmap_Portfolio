from typing import Annotated

PositiveInt = Annotated[int, "positive"]
ShortStr = Annotated[str, "len<=20"]


class InvalidPositiveInt(Exception):
    """Ошибка. Выбрасывается, если число меньше или рано нулю."""

    pass


class InvalidLenTest(Exception):
    """Ошибка. Выбрасывается, если длина строки больше или равно двадцати символам."""

    pass


def validate_positive(value: int) -> PositiveInt:
    if value <= 0:
        raise InvalidPositiveInt(f"Число {value} меньше или равно нулю.")

    return value


def validate_short(text: str) -> ShortStr:
    if len(text) > 20:
        raise InvalidLenTest(f'Строка "{text}" содержит 20 символов и более.')

    return text


def main() -> None:
    try:
        positive_int = validate_positive(1)
        short_str = validate_short("Hello")
    except (InvalidPositiveInt, InvalidLenTest) as error:
        print(f"> {error}")
    else:
        print(positive_int)
        print(short_str)


if __name__ == "__main__":
    main()
