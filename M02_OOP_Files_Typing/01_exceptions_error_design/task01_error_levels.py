import json
from pathlib import Path


class ConfigFileNotFound(Exception):
    pass


class ConfigInvalidJSON(Exception):
    pass


class ConfigMissingField(Exception):
    pass


class ConfigInvalidField(Exception):
    pass


class LimitNotPositive(Exception):
    pass


def json_config_reader(file_path: Path | str) -> int:
    """
    Читает JSON-файл конфигурации и возвращает числовое значение у ключа "limit".

    Args:
        file_path (Path | str): Путь к файлу конфигурации.

    Returns:
        int: Числовое значение ключа "limit" у конфигурации.

    Raises:
        ConfigFileNotFound: Если файл отсутствует.
        ConfigInvalidJSON: Если JSON-файл поврежден или невалиден.
        ConfigMissingField: Если нет ключа "limit".
        ConfigInvalidField: Если значение "limit" невозможно преобразовать в int.
        LimitNotPositive: Если limit <= 0.
    """
    # Блок отслеживания ошибок I/O + JSON
    try:
        with open(file_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

    except FileNotFoundError as error:
        raise ConfigFileNotFound(f"Файл конфигурации не найден: {file_path}") from error
    except json.JSONDecodeError as error:
        raise ConfigInvalidJSON(
            f"Файл {file_path} невалидный. Проверьте целостность файла."
        ) from error

    # Блок отслеживания валидации ключа "limit"
    try:
        raw_value = data["limit"]
        limit = int(raw_value)

        if limit <= 0:
            raise LimitNotPositive(f"Значение limit={raw_value} должно быть строго больше 0.")

        return limit
    except KeyError as error:
        raise ConfigMissingField(f"Ключ: {error.args[0]} отсутствует в конфигурации") from error
    except ValueError as error:
        raise ConfigInvalidField(f'Не удалось преобразовать "{raw_value}" в число.') from error


def main():
    file_path = "data/task01_data.json"

    try:
        result = json_config_reader(file_path)
    except (ConfigFileNotFound, ConfigInvalidJSON, ConfigMissingField, ConfigInvalidField) as error:
        print(error, f"\n> {error.__cause__}")
    except LimitNotPositive as error:
        print(f"> {error}")
    else:
        print(f"-Лимит данной конфигурации: {result}")


if __name__ == "__main__":
    main()
