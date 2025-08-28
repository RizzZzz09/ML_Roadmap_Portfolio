from pathlib import Path
from typing import Any, Dict, Iterable, List, Literal, Optional

HistoryEntry = Dict[str, Any]
Format = Literal["json", "pickle"]


def get_data_dir() -> Path:
    """Возвращает путь к директории хранения данных."""
    ...


def ensure_data_dir() -> Path:
    """Создает директорию хранения при необходимости и возвращает путь к ней."""
    ...


def get_history_path(fmt: Format = "json") -> Path:
    """Возвращает путь к файлу истории: history.json или history.pkl."""
    ...


def ensure_history_file(fmt: Format = "json") -> Path:
    """
    Проверка, что файл истории существует.
    Если нет — создает пустую историю [] соответствующим форматом.
    Возвращает путь к файлу.
    """
    ...


def load_history_json(path: Path) -> List[HistoryEntry]:
    """Загружает историю из JSON. Если файл не валидный или пустой возвращает []."""
    ...


def save_history_json(history: Iterable[HistoryEntry], path: Path) -> None:
    """Сохраняет историю в JSON."""
    ...


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
