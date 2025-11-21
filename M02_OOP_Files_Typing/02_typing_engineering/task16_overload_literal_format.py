from typing import Literal, overload


class InvalidMode(Exception):
    """Ошибка. Выбрасывается, если был выбран некорректный режим работы функции."""

    pass


@overload
def format_value(value: str, mode: Literal["strip"]) -> str: ...


@overload
def format_value(value: str, mode: Literal["lower"]) -> str: ...


@overload
def format_value(value: str, mode: Literal["len"]) -> int: ...


def format_value(value: str, mode: Literal["strip", "lower", "len"]) -> str | int:
    if mode == "strip":
        return value.strip()
    elif mode == "lower":
        return value.lower()
    elif mode == "len":
        return len(value)
    else:
        raise InvalidMode(f'Данный режим работы "{mode}" не поддерживается.')


def main() -> None:
    text = "Hello"

    try:
        result = format_value(text, "strip")
    except InvalidMode as error:
        print(f"> {error}")
    else:
        print(result)


if __name__ == "__main__":
    main()
