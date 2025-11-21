from pathlib import Path
from typing import Literal, TextIO


class InvalidMode(Exception):
    """Ошибка. Выбрасывается, если указанный пользователем режим чтения файла не поддерживается."""

    pass


def open_test_file(path: Path | str, mode: Literal["r", "w", "a"]) -> TextIO:
    if mode not in ("r", "w", "a"):
        raise InvalidMode(f"Указан неверный режим открытия файла {mode}.")

    file = open(path, mode)
    return file


def main() -> None:
    file_path = "data/text.txt"

    try:
        result = open_test_file(file_path, "r")
    except InvalidMode as error:
        print(f"> {error}")
    else:
        print(result)


if __name__ == "__main__":
    main()
