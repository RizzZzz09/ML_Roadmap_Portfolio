import os
from pathlib import Path


def get_data_dir(flag_path: str | None = None) -> Path:
    """
    Определяет путь к папке для хранения данных.

    Приоритет:
    1. Путь из аргумента функции (флаг командной строки).
    2. Переменная окружения CALC_DIR.
    3. Домашняя директория пользователя + ".calc_data".

    Args:
        flag_path (str | None): Путь, переданный из аргумента командной строки (--history-dir).

    Returns:
        Path: Путь к папке.
    """
    if flag_path:
        return Path(flag_path)

    env_path = os.getenv("CALC_DIR")
    if env_path:
        return Path(env_path)

    return Path.home() / ".calc_data"


def ensure_data_dir(path: Path) -> bool | str:
    """
    Проверяет существование директории и создаёт её при необходимости.

    Args:
        path (Path): Путь к папке пользователя.

    Returns:
        bool: True, если директория существует или была создана.
        str: Сообщение об ошибке, если по пути найден файл вместо директории.
    """
    if path.exists():
        if path.is_dir():
            return True
        else:
            return f"Cannot use '{path}': this is a file, not a directory"
    else:
        path.mkdir(parents=True, exist_ok=True)
        return True


def get_history_path(data_dir: Path) -> Path:
    """
    Возвращает путь к файлу, для сохранения данных.

    Args:
        data_dir (Path): Директория для сохранения.

    Returns:
        Path: Путь к файлу.
    """
    return Path(data_dir) / "history.json"


def ensure_history_file(history_path: Path) -> bool | str:
    """
    Гарантирует наличие файла истории: создаёт пустой, если его нет.

    Args:
        history_path (Path): Путь к файлу истории.

    Returns:
        bool: True, если файл существует или был создан.
        str: Сообщение об ошибке, если по этому пути уже существует директория.
    """
    if history_path.exists():
        if history_path.is_file():
            return True
        else:
            return f"Cannot create history file '{history_path}': path points to a directory"
    else:
        history_path.touch(exist_ok=True)
        return True
