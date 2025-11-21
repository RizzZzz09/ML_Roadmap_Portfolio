from typing import Literal, Protocol


class InvalidMode(Exception):
    """Ошибка. Пробрасывается, если пользователь выбрал не существующий режим."""

    pass


class Formatter(Protocol):
    def format(self, message: str, mode: Literal["upper", "lower"]) -> str: ...


class TextFormatter:
    def format(self, message: str, mode: Literal["upper", "lower"]) -> str:
        if mode == "upper":
            return message.upper()
        elif mode == "lower":
            return message.lower()
        else:
            raise InvalidMode(f'Режим работы "{mode}" не поддерживается.')


def apply_format(formatter: Formatter, message: str, mode: Literal["upper", "lower"]) -> str:
    return formatter.format(message, mode)


def main() -> None:
    message = "How are you?"
    test_formatter = TextFormatter()

    try:
        result_upper = apply_format(test_formatter, message, "upper")
        result_lower = apply_format(test_formatter, message, "lower")
    except InvalidMode as error:
        print(f"> {error}")
    else:
        print(result_upper)
        print(result_lower)


if __name__ == "__main__":
    main()
