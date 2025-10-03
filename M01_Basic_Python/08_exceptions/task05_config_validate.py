import json

file_path = "data/config.json"
expected_types = {"host": str, "port": int, "debug": bool}


class ConfigValidationError(Exception):
    """Ошибка. Неверный формат содержимого у файла."""

    pass


def validate(config: dict[str, str | int | bool]):
    for key, expected_type in expected_types.items():
        if not isinstance(config.get(key), expected_type):
            raise ConfigValidationError("Validation failed. Invalid file structure.")


def main():
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            validate(data)
    except FileNotFoundError as error:
        print(error)
    except json.JSONDecodeError as error:
        print(error)
    except ConfigValidationError as error:
        print(error)
    else:
        print("Validation successful!")


if __name__ == "__main__":
    main()
