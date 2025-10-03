class ParseError(Exception):
    """Ошибка преобразования в число."""

    pass


def parser(number: str) -> int:
    try:
        result = int(number)
    except ValueError as error:
        raise ParseError(f"Failed to convert '{number}' to a number") from error
    else:
        return result


def main():
    while True:
        user_input = input("Enter any number: ").lower().strip()
        if user_input == "q":
            break
        result = parser(user_input)
        print(result)


if __name__ == "__main__":
    main()
