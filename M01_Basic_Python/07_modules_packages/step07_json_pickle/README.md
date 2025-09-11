# M1.7 — Modules & Packages
## Step 07 — Сериализация (JSON и Pickle)

В этом шаге мы расширяем функционал CLI-калькулятора и учимся сохранять историю операций в файлы разных форматов.

---

## 📘 Теория

### Зачем это нужно
Когда программа работает, все данные живут в оперативной памяти (RAM). После завершения работы они исчезают.
Чтобы данные сохранялись между запусками (например, история калькулятора), их нужно записывать в файл.

👉 Для этого используется **сериализация** — преобразование объектов Python в формат для хранения.

В Python есть два главных инструмента:
- **JSON** — универсальный текстовый формат;
- **Pickle** — бинарный формат, «родной» для Python.

---

### JSON

**JSON (JavaScript Object Notation)** — текстовый формат хранения данных «ключ-значение».
Популярен в API, конфигурационных файлах и логах.

Пример JSON:
```json
[
  {"operation": "add", "operands": [2, 3], "result": 5},
  {"operation": "sub", "operands": [10, 7], "result": 3}
]
```

**Поддерживаемые типы:**
- `dict` → `{}`
- `list`, `tuple` → `[]`
- `str` → строка
- `int`, `float` → число
- `bool` → `true`/`false`
- `None` → `null`

**Модуль `json`:**
```python
import json

data = {"operation": "add", "operands": [2, 3], "result": 5}

# Сохранение
with open("history.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Загрузка
with open("history.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
```

Важные параметры:
- `ensure_ascii=False` — сохраняет кириллицу нормально;
- `indent=2` — форматирование;
- `sort_keys=True` — сортировка ключей.

---

### Pickle

**Pickle** — бинарный формат сериализации Python-объектов.
Главное отличие: умеет сохранять почти всё, включая кастомные классы, функции и объекты.

**Минусы:**
- Формат «закрытый» (только Python);
- Не читаем человеком;
- Небезопасен (нельзя загружать из непроверенных источников).

**Модуль `pickle`:**
```python
import pickle

data = {"operation": "mul", "operands": [4, 5], "result": 20}

# Сохранение
with open("history.pkl", "wb") as f:
    pickle.dump(data, f)

# Загрузка
with open("history.pkl", "rb") as f:
    loaded = pickle.load(f)

print(loaded)
```

---

### Сравнение форматов

| Свойство       | JSON                 | Pickle                |
|----------------|----------------------|-----------------------|
| Формат         | Текстовый (UTF-8)    | Бинарный              |
| Читаемость     | ✅ Читаемый          | ❌ Нечитаемый          |
| Совместимость  | ✅ Межъязыковой      | ❌ Только Python       |
| Типы данных    | Ограниченные         | Почти любые           |
| Безопасность   | ✅ Безопасен         | ❌ Опасен при загрузке |
| Скорость       | Средняя              | Немного быстрее       |

👉 Вывод:
- для реальных приложений и истории калькулятора → **JSON**,
- для экспериментов и сугубо Python-объектов → **Pickle**.

---

## 🛠 Практика

Мы добавили в проект поддержку сериализации и реализовали:

- папку `data/` для хранения файлов истории;
- функции в `storage.py`:
  - `get_data_dir`, `ensure_data_dir`;
  - `get_history_path`, `ensure_history_file`;
  - `load_history_json`, `save_history_json`;
  - `load_history_pickle`, `save_history_pickle`;
  - `load_history`, `save_history` (унифицированный интерфейс).

Формат выбирается через флаг CLI `--format {json,pickle}`.
История хранится в виде списка словарей:
```python
{
  "operation": "add",
  "operands": [2, 3],
  "result": 5
}
```

---

## ▶️ Запуск и примеры

```bash
# Показ пустой истории (JSON по умолчанию)
python -m app.main --show-history
# []

# Выполнение операций
python -m app.main add 2 3 --show-history
python -m app.main sub 10 7 --show-history

# Использование Pickle
python -m app.main mul 4 5 --format pickle --show-history

# Возврат в JSON (независимая история)
python -m app.main --show-history

# Очистка истории
python -m app.main --clear-history --show-history
# []
```

---

## 📂 Структура проекта (шаг 7)

```
step07_json_pickle/
├─ app/
│  ├─ core/
│  │  └─ operations.py
│  ├─ utils/
│  │  └─ storage.py
│  └─ main.py
├─ data/
│  ├─ history.json
│  └─ history.pkl
└─ README.md
```

---

## ✅ Критерии готовности

- Освоили работу с **сериализацией** в Python (JSON и Pickle).
- Научились сохранять историю между запусками.
- Реализовали флаги CLI:
  - `--show-history` — показать историю,
  - `--clear-history` — очистить историю,
  - `--format` — выбор формата хранения.


## 🛟 Устранение неполадок
_(добавить частые ошибки)_
