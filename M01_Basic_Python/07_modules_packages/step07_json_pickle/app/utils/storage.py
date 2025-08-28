import json
import pickle
from pathlib import Path
from typing import Any, Dict, Iterable, List, Literal, Optional

HistoryEntry = Dict[str, Any]
Format = Literal["json", "pickle"]


def get_data_dir() -> Path:
    """
    Возвращает путь к директории хранения данных.

    Returns:
        Path: Путь к папке с сохраненными файлами.
    """
    return Path(__file__).resolve().parents[2] / "data"


def ensure_data_dir() -> Path:
    """
    Создает директорию хранения при необходимости и возвращает путь к ней.

    Returns:
        Path: Путь к папке с сохраненными файлами.
    """
    folder = get_data_dir()
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def get_history_path(fmt: Format = "json") -> Path:
    """
    Возвращает путь к файлу истории: history.json или history.pkl.

    Returns:
        Path: Путь к файлу сохранения history.json или history.pkl
    """
    dir_path = get_data_dir()
    if fmt == "json":
        return dir_path / "history.json"
    elif fmt == "pickle":
        return dir_path / "history.pkl"


def ensure_history_file(fmt: Format = "json") -> Path:
    """
    Проверка, что файл истории существует.
    Если нет — создает пустую историю [] соответствующим форматом.
    Возвращает путь к файлу.

    Returns:
        Path: Путь к файлу сохранения history.json или history.pkl.
    """
    ensure_data_dir()
    path = get_history_path(fmt)

    if path.exists():
        return path
    else:
        if fmt == "json":
            with open(path, "w", encoding="utf-8") as file:
                json.dump([], file, ensure_ascii=False, indent=2)
        elif fmt == "pickle":
            with open(path, "wb") as file:
                pickle.dump([], file)
        return path


def load_history_json(path: Path) -> List[HistoryEntry]:
    """
    Загружает историю из JSON. Если файл не валидный или пустой возвращает [].

    Returns:
        List: Список истории операций.
    """
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data if isinstance(data, list) else []


def save_history_json(history: Iterable[HistoryEntry], path: Path) -> None:
    """Сохраняет историю в JSON."""
    data = list(history)
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def load_history_pickle(path: Path) -> List[HistoryEntry]:
    """Загружает историю из Pickle. Если файл не валидный или пустой возвращает []."""
    ...


def save_history_pickle(history: Iterable[HistoryEntry], path: Path) -> None:
    """Сохраняет историю в Pickle"""
    ...


def load_history(path: Optional[Path] = None, fmt: Format = "json") -> List[HistoryEntry]:
    """Единая точка загрузки по формату."""
    ...


def save_history(
    history: Iterable[HistoryEntry], path: Optional[Path] = None, fmt: Format = "json"
) -> None:
    """Единая точка сохранения по формату."""
    ...
