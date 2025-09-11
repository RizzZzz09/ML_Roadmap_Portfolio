# M1.7 — Modules & Packages
## Step 08 — Работа с датами и временем (`datetime`)

## 📘 Полная теория — datetime в Python

### 1. Базовые классы модуля `datetime`
- `datetime` — дата + время.
- `date` — только дата (год, месяц, день).
- `time` — только время (часы, минуты, секунды и т.д.).

```python
from datetime import datetime, date

now = datetime.now()    # текущее дата и время
today = date.today()    # только дата
```

---

### 2. Получение текущего времени
```python
from datetime import datetime

now = datetime.now()         # локальное текущее время
utc_now = datetime.utcnow()  # UTC-время (naive, без таймзоны)
```

---

### 3. Форматирование дат — `strftime`
```python
dt = datetime(2025, 8, 31, 20, 45)
print(dt.strftime("%Y-%m-%d %H:%M:%S"))  # 2025-08-31 20:45:00
```

| Код | Значение             | Пример          |
|-----|----------------------|----------------|
| `%Y` | Год (4 цифры)         | 2025 |
| `%m` | Месяц (01–12)         | 08 |
| `%d` | День (01–31)           | 31 |
| `%H` | Часы (00–23)           | 20 |
| `%M` | Минуты (00–59)         | 45 |
| `%S` | Секунды (00–59)        | 00 |
| `%A` | День недели            | Sunday |
| `%B` | Название месяца        | August |

---

### 4. Разбор строк — `strptime`
```python
text = "31-12-2025 23:59"
dt = datetime.strptime(text, "%d-%m-%Y %H:%M")
```

---

### 5. Разница между датами — `timedelta`
```python
from datetime import timedelta

now = datetime.now()
week = now + timedelta(days=7)
print(week - now)  # 7 days, 0:00:00
```

---

### 6. timestamp ↔ datetime
```python
now = datetime.now()
ts = now.timestamp()                  # datetime → timestamp (float)
dt = datetime.fromtimestamp(ts)       # timestamp → datetime
```

---

### 7. Часовые пояса — `timezone` и `ZoneInfo`
```python
from datetime import timezone, timedelta
from zoneinfo import ZoneInfo

utc = datetime.now(timezone.utc)
riga = datetime.now(ZoneInfo("Europe/Riga"))
```

---

### 8. aware vs naive
```python
dt = datetime.now()                     # naive
dt_aware = datetime.now(timezone.utc)   # aware (UTC)
```

---

### 9. ISO 8601
```python
dt = datetime.now(timezone.utc)
print(dt.isoformat())  # 2025-09-03T16:23:40.345305+00:00
```

---

## 🧪 Практика — задачи

🔹 **Task 01 — Current datetime**
📂 `task01_now.py`
Вывести текущую дату, время и datetime в разных форматах (`%Y-%m-%d`, `%H:%M:%S`, `%Y-%m-%d %H:%M:%S`).

🔹 **Task 02 — Parse string**
📂 `task02_parse_str.py`
Преобразовать строку `"31-12-2025 23:59"` в `datetime` и вывести год, месяц, день, час и минуту.

🔹 **Task 03 — Days until New Year**
📂 `task03_new_year.py`
Посчитать количество дней до следующего Нового года.

🔹 **Task 04 — Date arithmetic**
📂 `task04_timedelta.py`
К сегодняшней дате прибавить 7, 30 и 365 дней и вывести результаты.

🔹 **Task 05 — Timestamp conversion**
📂 `task05_timestamp.py`
Преобразовать `datetime` в `timestamp` и обратно, вывести оба значения.

🔹 **Task 06 — Timezones**
📂 `task06_timezones.py`
Вывести текущее время в `UTC` и `Europe/Riga` (через `timezone` и `ZoneInfo`).

🔹 **Task 07 — Format short**
📂 `task07_format_short.py`
Написать функцию `format_short(dt)` → строка вида `31/08/2025, 20:45`.

🔹 **Task 08 — Format long**
📂 `task08_format_long.py`
Написать функцию `format_long(dt)` → строка вида
`Sunday, 31 August 2025, 20:45:00 GMT+03:00`.

🔹 **Task 09 — Countdown timer**
📂 `task09_countdown.py`
Запросить у пользователя число секунд, вести обратный отсчёт и выводить оставшееся время каждую секунду.

---

## 🧮 Интеграция в калькулятор
В `app/main.py` добавлено:
- `--time-format [iso|short|long]`
- `--tz Europe/Riga`
- `--since <dt>` и `--until <dt>` — фильтрация по времени

```bash
python -m app.main --clear-history --format json
python -m app.main add 2 3 --format json
python -m app.main --show-history --format json --time-format short --tz Europe/Riga
python -m app.main --show-history --format json --since "03/09/2025, 19:23" --tz Europe/Riga
```

---

## ▶️ Запуск программ из practice
```bash
python practice/task01_now.py
python practice/task02_parse_str.py
python practice/task03_new_year.py
python practice/task04_timedelta.py
python practice/task05_timestamp.py
python practice/task06_timezones.py
python practice/task07_format_short.py
python practice/task08_format_long.py
python practice/task09_countdown.py
```


## 📁 Структура шага
_(добавить дерево файлов)_


## 🛟 Устранение неполадок
_(добавить частые ошибки)_


## ✅ Критерии готовности
_(добавить чеклист)_
