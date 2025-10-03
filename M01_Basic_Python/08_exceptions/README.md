# M1.8 — Исключения
В этом модуле ты освоишь обработку ошибок в Python: конструкции `try/except/else/finally`, создание собственных исключений, проброс и подавление ошибок.

---

## 🎯 Что ты освоишь
- Обрабатывать ошибки с помощью `try/except/else/finally`
- Создавать собственные классы исключений
- Использовать проброс (`raise`) и цепочки исключений (`raise ... from ...`)
- Применять контекстные менеджеры и конструкцию `with` для безопасной работы с ресурсами
- Подавлять ожидаемые ошибки с помощью `contextlib.suppress`
- Применять best practices для «человечного» взаимодействия с пользователем

---

## 📘 Полная теория

### 1. Основы обработки ошибок
В Python ошибки (исключения) выбрасываются, когда что-то идёт не так. Чтобы программа не падала, мы можем их обработать.

```python
try:
    number = int(input("Enter number: "))
except ValueError:
    print("Вы ввели не число!")
```

🔹 `try` — блок кода, где может произойти ошибка
🔹 `except` — перехват конкретной ошибки
🔹 `else` — выполняется, если ошибок не было
🔹 `finally` — выполняется всегда (например, закрытие файлов или соединений)

```python
try:
    f = open("data.txt")
    data = f.read()
except FileNotFoundError:
    print("Файл не найден")
else:
    print("Файл успешно прочитан")
finally:
    f.close()
```

---

### 2. Создание собственных исключений
Мы можем описывать свои ошибки, чтобы код был понятнее:

```python
class NegativeNumberError(Exception):
    """Ошибка: число меньше нуля."""
    pass
```

Использование:

```python
def sqrt_strict(x: int) -> float:
    if x < 0:
        raise NegativeNumberError("Нельзя извлекать корень из отрицательного числа")
    return x ** 0.5
```

---

### 3. Проброс и повторное выбрасывание ошибок
Если функция не может обработать ошибку сама, её нужно пробросить дальше.

```python
def parse_number(s: str) -> int:
    try:
        return int(s)
    except ValueError as e:
        print(f"Ошибка парсинга: {e}")
        raise   # проброс ошибки выше
```

Вызов в `main` может поймать эту же ошибку:
```python
try:
    num = parse_number("abc")
except ValueError:
    print("Введено некорректное число")
```

---

### 4. Цепочка исключений (`raise ... from e`)
Иногда мы хотим заменить ошибку на свою, но сохранить причину:

```python
class ParseError(Exception):
    pass

def parse_int(s: str) -> int:
    try:
        return int(s)
    except ValueError as e:
        raise ParseError(f"Не удалось преобразовать '{s}' в число") from e
```

Вывод покажет сначала `ValueError`, а затем `ParseError` как «причинённую» ошибку.

---

### 5. `finally` и `with open`
`finally` часто используют для гарантированного освобождения ресурсов:

```python
f = None
try:
    f = open("data.txt")
    data = f.read()
finally:
    if f is not None:
        f.close()
```

Но лучше использовать `with`, который сам закрывает ресурс:

```python
with open("data.txt") as f:
    data = f.read()
```

---

### 6. Подавление ожидаемых ошибок
Если ошибка ожидаема и не критична (например, папка уже существует), можно её «подавить»:

```python
from contextlib import suppress
import os

with suppress(FileExistsError):
    os.mkdir("data/testdir")
```

---

### 7. Повторные попытки (retry, backoff)
Иногда нужно повторять операцию с задержкой, если она падает:

```python
import time, random

def unstable():
    if random.random() < 0.5:
        raise RuntimeError("Сбой")
    return "Успех"

def retry(fn, attempts=3, base_delay=0.5):
    for i in range(attempts):
        try:
            return fn()
        except RuntimeError as e:
            if i == attempts - 1:
                raise
            delay = base_delay * (2 ** i)
            print(f"Ошибка: {e}, ждём {delay} секунд...")
            time.sleep(delay)
```

---

### 8. Best practices
- Лови конкретные ошибки (`ValueError`, `FileNotFoundError`), а не `except Exception`.
- Используй `with` для работы с файлами и ресурсами.
- Не гаси все ошибки без разбора (`suppress(Exception)` — плохая практика).
- Используй кастомные исключения для бизнес-логики.
- Для пользователя ошибки должны быть дружелюбными, а для логов — максимально информативными.
- Держи `try` блоки как можно короче.

---

## 📁 Структура модуля
```
08_exceptions/
├── data/
│   ├── test_dir
│   ├── config.json
│   ├── missing.txt
│   ├── prices.csv
│   ├── raw.txt
│   └── text.txt
├── task01_safe_input.py
├── task02_division.py
├── task03_file_read.py
├── task04_custom_exception.py
├── task05_config_validate.py
├── task06_normalize_prices.py
├── task07_reraise.py
├── task08_retry_backoff.py
├── task09_safe_file.py
├── task10_exception_chain.py
├── task11_suppress.py
└── task12_console_calc.py
```

---

## 🧩 Задания
1. **Безопасный ввод числа** — обработка `ValueError`
2. **Деление с обработкой нуля** — перехват `ZeroDivisionError`
3. **Чтение файла с `else/finally`** — учимся правильно закрывать ресурсы
4. **Своё исключение `NegativeNumberError`** — кастомные классы ошибок
5. **Валидация конфигурации JSON** — `ConfigValidationError`
6. **Нормализация списка цен (CSV)** — `DataFormatError` и `DataQualityError`
7. **Проброс исключений (re-raise)** — логируем и передаём выше
8. **Ретраи с backoff** — повторные попытки при сбоях
9. **Безопасное открытие файла** — `try/except/finally`
10. **Цепочка исключений** — `raise ... from e`
11. **Подавление ошибок** — `contextlib.suppress`
12. **Калькулятор** — практика со всеми видами ошибок

---

## ▶️ Как запускать
Пример запуска любой задачи:
```bash
python task01_safe_input.py
```

Для калькулятора (Task 12):
```bash
python task12_console_calc.py
```

---

## ✅ Критерии готовности
- Все 12 задач решены и проходят тестовые сценарии
- Собственные исключения используются там, где нужно
- `try/except/else/finally` применены корректно
- Ошибки пробрасываются и логируются
- Подавление (`suppress`) и цепочки (`from e`) показаны в работе
- Калькулятор работает в цикле, не падает, дружелюбно сообщает об ошибках

---

## 🛟 Устранение неполадок
- **`UnboundLocalError` в `finally`** — инициализируй переменную до `try` (`f = None`)
- **`suppress(Exception)` гасит всё** — используй только конкретные типы (`FileExistsError`)
- **`isdigit()` и отрицательные числа** — лучше парсить через `int()` и ловить `ValueError`
- **CSV парсинг ломается** — применяй `csv.DictReader`, а не разбиение строк вручную
- **Калькулятор падает при неверной операции** — перехватывай `OperationNotSupportedError` и выводи подсказку
