file_path = "data/raw.txt"


def load(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = file.read()
    except FileNotFoundError as error:
        print(f"Error: File not found {error}")
        raise
    else:
        return data


def parse(text: str) -> list[int]:
    try:
        parse_text = [int(number) for number in text.split()]
    except ValueError as error:
        print(f"Error: Failed to convert to number {error}")
        raise
    else:
        return parse_text


def process(number_list: list[int]) -> float:
    a = number_list[0]
    b = number_list[1]
    c = number_list[2]
    d = number_list[3]
    try:
        result = (a + b) / (c + d)
    except ZeroDivisionError as error:
        print(f"Error: You can't divide by zero {error}")
        raise
    else:
        return result


def main():
    try:
        raw = load(file_path)
        data = parse(raw)
        result = process(data)
    except ValueError as error:
        print(f"Error: {error}")
    except FileNotFoundError as error:
        print(f"Error {error}")
    except ZeroDivisionError as error:
        print(f"Error: {error}")
    else:
        print(result)


if __name__ == "__main__":
    main()
