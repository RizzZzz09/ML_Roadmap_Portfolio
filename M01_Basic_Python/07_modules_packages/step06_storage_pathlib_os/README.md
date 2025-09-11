# M1.7 — Modules & Packages
## Step 06 — Хранилище на `pathlib` + `os` — директория данных и history.json

> Цель шага: подготовить **инфраструктуру хранения** — выбрать/создать директорию и файл истории, не записывая данные (запись будет в Step 07).

---

### 🎯 Что ты освоишь
- Работа с путями через `pathlib.Path` (кроссплатформенно).
- Переменные окружения через `os.getenv`.
- Идемпотентное создание директорий/файлов (`mkdir`, `touch`).
- Добавление CLI‑флагов для настройки места хранения.

---

## 📘 Полная теория

### 1) Pathlib essentials
```python
from pathlib import Path

d = Path.home() / ".calc_data"              # дефолтная директория
d.exists(); d.is_dir(); d.is_file()
d.mkdir(parents=True, exist_ok=True)        # создать директорию

f = d / "history.json"
f.touch(exist_ok=True)                      # создать пустой файл
f.resolve()                                 # абсолютный путь
```

### 2) Переменные окружения
```python
import os
custom = os.getenv("CALC_DIR")  # None, если не задано
```
Приоритет путей (рекомендуемый):
1) флаг `--history-dir`,
2) `CALC_DIR` из окружения,
3) `Path.home() / ".calc_data"` по умолчанию.

### 3) Идемпотентность
- Все операции создания должны быть безопасны при повторном запуске.
- Проверяй коллизии: по пути к файлу может оказаться директория.

---

## 📁 Структура шага
```
M01_Basic_Python/07_modules_packages/step6_storage_pathlib_os/
└─ app/
   ├─ __init__.py
   ├─ main.py
   ├─ core/
   │  ├─ __init__.py
   │  └─ operations.py
   └─ utils/
      ├─ __init__.py
      └─ storage.py   # функции для путей/директорий/файлов
```

---

## 🧩 Задания

### 1) `utils/storage.py`
Реализуй функции:
- `get_data_dir(flag_path: str | None = None) -> Path`
  Возвращает директорию хранения (флаг → env `CALC_DIR` → `~/.calc_data`).
- `ensure_data_dir(path: Path) -> bool | str`
  Создаёт директорию при необходимости; если по пути **файл** — верни строку‑ошибку.
- `get_history_path(data_dir: Path) -> Path`
  Возвращает `data_dir / "history.json"`.
- `ensure_history_file(history_path: Path) -> bool | str`
  Создаёт пустой файл при необходимости; если по пути **директория** — верни строку‑ошибку.

### 2) Интеграция в `app/main.py`
Добавь флаги:
- `--history-dir PATH` — пользовательский путь к каталогу хранения;
- `--show-history-path` — напечатать абсолютный путь к истории и завершить работу.

Перед выполнением операции:
1) `data_dir = get_data_dir(args.history_dir)`
2) `ensure_data_dir(data_dir)`
3) `history = get_history_path(data_dir)`
4) `ensure_history_file(history)`
5) если `--show-history-path` → вывести `history.resolve()` и `return`

---

## ▶️ Как запускать
Из папки шага:
```bash
# дефолтный путь (~/.calc_data)
python -m app.main add 1 2 --show-history-path

# через переменную окружения (PowerShell)
$env:CALC_DIR="C:\Temp\my_calc"
python -m app.main add 1 2 --show-history-path

# флаг перекрывает env
python -m app.main add 5 7 --history-dir "C:\Temp\my_calc2" --show-history-path
```

---

## ✅ Критерии готовности
- [x] При первом запуске создаётся директория и пустой `history.json`.
- [x] `--show-history-path` печатает абсолютный путь.
- [x] Работают три сценария выбора директории (флаг > env > дефолт).
- [x] Никаких трассировок/исключений — только понятные сообщения при ошибках.

---

## 🛟 Устранение неполадок

**`ModuleNotFoundError: No module named 'app'`**
— Запускай из родителя папки `app/` (каталог шага).

**По пути к директории оказался файл**
— `ensure_data_dir` должен вернуть строку‑ошибку; выведи её и заверши работу.

**По пути к файлу истории оказалась директория**
— `ensure_history_file` должен вернуть строку‑ошибку.
