# Task 02 — API Error Contract

## Функция

`json_config_reader(path: str | Path) -> int`

## Что делает

Читает JSON-конфиг, достаёт значение `limit`, конвертирует в `int` и применяет правило `limit > 0`.

## Returns

- `int` — валидное значение `limit`.

## Raises

| Исключение           | Когда поднимается                                   |
|----------------------|-----------------------------------------------------|
| `ConfigFileNotFound` | файл не существует по указанному пути               |
| `ConfigInvalidJSON`  | файл существует, но JSON повреждён / невалиден      |
| `ConfigMissingField` | в JSON нет ключа `"limit"`                          |
| `ConfigInvalidField` | значение по ключу `"limit"` нельзя привести к `int` |
| `LimitNotPositive`   | `limit <= 0` нарушает бизнес-правило                |

## Примечание

Функция *не* пропускает наружу системные исключения `FileNotFoundError`, `JSONDecodeError`, `KeyError`, `ValueError`.
Эти ошибки переводятся в доменные через `raise ... from ...`.

---
