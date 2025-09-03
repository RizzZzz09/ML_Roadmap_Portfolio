from datetime import datetime
from zoneinfo import ZoneInfo


def from_iso(date: str) -> datetime:
    """
    Преобразует ISO-8601 строку в объект datetime (aware).

    Args:
        date: Строка времени в формате ISO-8601.

    Returns:
        Объект datetime с учётом смещения (UTC или другой TZ).
    """
    return datetime.fromisoformat(date)


def to_local(dt: datetime, tz_name: str) -> datetime:
    """
    Переводит время в указанный часовой пояс.

    Args:
        dt: Время для преобразования.
        tz_name: Имя часового пояса.

    Returns:
        Время в целевом часовом поясе.
    """
    return dt.astimezone(ZoneInfo(tz_name))


def format_short(dt: datetime) -> str:
    """
    Возвращает строку с коротким форматом времени.

    Args:
        dt: Время для преобразования.

    Returns:
        Короткая форма записи времени.
    """
    return dt.strftime("%d/%m/%Y, %H:%M")


def format_long(dt: datetime) -> str:
    """
    Возвращает строку с длинным форматом времени.

    Args:
        dt: Время для преобразования.

    Returns:
        Длинная форма записи времени.
    """
    base = dt.strftime("%A, %d %B %Y, %H:%M:%S")

    offset = dt.utcoffset()
    if offset is None:
        gmt = "GMT"
    else:
        total_minutes = int(offset.total_seconds() // 60)
        sign = "+" if total_minutes >= 0 else "-"
        hours, minutes = divmod(abs(total_minutes), 60)
        gmt = f"GMT{sign}{hours:02}:{minutes:02}"

    return f"{base} {gmt}"
