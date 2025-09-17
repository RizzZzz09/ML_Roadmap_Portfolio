# M1.7 — Itertools (`itertools` module)

## 📘 Теория — Модуль `itertools`

Модуль `itertools` — часть стандартной библиотеки Python, предоставляющая **ленивые (lazy) итераторы** для генерации,
комбинирования и фильтрации последовательностей.

**Ленивые итераторы** не хранят все элементы в памяти — они создают их **по запросу**, что делает работу с большими или
бесконечными последовательностями очень эффективной.

---

### 📈 Бесконечные итераторы

| Функция                | Описание                                                         |
|------------------------|------------------------------------------------------------------|
| `count(start, step)`   | Бесконечная арифметическая прогрессия (`start`, `start+step`, …) |
| `cycle(iterable)`      | Бесконечно повторяет элементы `iterable`                         |
| `repeat(elem, n=None)` | Повторяет `elem` `n` раз или бесконечно                          |

```python
from itertools import count, cycle, repeat

for x in count(10, 5):
    print(x)
    if x > 30:
        break

colors = cycle(['red', 'green', 'blue'])
print(next(colors))  # red
print(next(colors))  # green

for x in repeat('A', 3):
    print(x)  # A A A
```

---

### 🧩 Комбинаторные генераторы

| Функция                                      | Описание                                |
|----------------------------------------------|-----------------------------------------|
| `product(a, b, repeat=1)`                    | Декартово произведение (все комбинации) |
| `permutations(iterable, r)`                  | Перестановки длиной `r`                 |
| `combinations(iterable, r)`                  | Сочетания без повторений                |
| `combinations_with_replacement(iterable, r)` | Сочетания с повторениями                |

```python
from itertools import product, permutations, combinations

print(list(product([1, 2], ['A', 'B'])))
# [(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')]

print(list(permutations('abc', 2)))
# [('a', 'b'), ('a', 'c'), ('b', 'a'), ...]

print(list(combinations('abc', 2)))
# [('a', 'b'), ('a', 'c'), ('b', 'c')]
```

---

### 🧮 Фильтрация и срезы

| Функция                               | Описание                                   |
|---------------------------------------|--------------------------------------------|
| `islice(iterable, start, stop, step)` | Срез итератора как у списка                |
| `compress(data, selectors)`           | Выбирает элементы, где `selectors == True` |
| `filterfalse(func, iterable)`         | Оставляет элементы, где `func == False`    |
| `dropwhile(func, iterable)`           | Пропускает пока `func == True`             |
| `takewhile(func, iterable)`           | Берёт пока `func == True`                  |

```python
from itertools import islice, compress, filterfalse

nums = range(10)
print(list(islice(nums, 2, 8, 2)))  # [2, 4, 6]

data = ['a', 'b', 'c', 'd']
selectors = [1, 0, 1, 0]
print(list(compress(data, selectors)))  # ['a', 'c']

print(list(filterfalse(lambda x: x % 2, range(6))))  # [0, 2, 4]
```

---

### ⚡ Комбинирование нескольких итераторов

| Функция                             | Описание                                      |
|-------------------------------------|-----------------------------------------------|
| `chain(a, b, c)`                    | Соединяет несколько итерируемых объектов      |
| `zip_longest(a, b, fillvalue=None)` | Как `zip`, но дополняет до максимальной длины |

```python
from itertools import chain, zip_longest

a = [1, 2]
b = ['x', 'y', 'z']
print(list(chain(a, b)))  # [1, 2, 'x', 'y', 'z']

print(list(zip_longest(a, b, fillvalue='-')))
# [(1, 'x'), (2, 'y'), ('-', 'z')]
```

---

### 🧠 Расширенные функции — с примерами

```python
from itertools import accumulate, starmap, pairwise, tee, groupby, batched
import operator

# accumulate: кумулятивные суммы/произведения
nums = [1, 2, 3, 4]
print(list(accumulate(nums)))  # [1, 3, 6, 10]
print(list(accumulate(nums, operator.mul)))  # [1, 2, 6, 24]

# starmap: распаковка аргументов из кортежей
pairs = [(1, 2), (3, 4), (5, 6)]
print(list(starmap(operator.add, pairs)))  # [3, 7, 11]

# pairwise: соседние пары (x, x+1)
print(list(pairwise([10, 20, 30, 40])))  # [(10, 20), (20, 30), (30, 40)]

# tee: независимые копии итератора
import itertools as it

a, b = tee(range(3), 2)
print(list(a), list(b))  # [0, 1, 2] [0, 1, 2]

# groupby: группировка подряд идущих элементов по ключу
animals = sorted(['cat', 'cow', 'dog', 'duck'])
for key, group in groupby(animals, key=lambda s: s[0]):
    print(key, list(group))  # c ['cat','cow']; d ['dog','duck']

# batched: разбиение на чанки фиксированного размера
print(list(batched(range(1, 10), 3)))  # [(1,2,3), (4,5,6), (7,8,9)]
```

## 💻 Задачи

### 🔹 **Task 01 — Count / Cycle / Repeat**

📂 `task01_count_cycle_repeat.py`
**Цель:** Освоить бесконечные итераторы count/cycle/repeat на простых примерах.
**Ключевые идеи:** ленивые итераторы, islice, остановка по условию.
---

### 🔹 **Task 02 — Комбинаторика**

📂 `task02_combinations.py`
**Цель:** Получить product/permutations/combinations.
**Ключевые идеи:** product, permutations, combinations, combinations_with_replacement.

---

### 🔹 **Task 03 — Фильтрация и срезы**

📂 `task03_filter_slice.py`
**Цель:** Отфильтровать и взять срезы элементов из потока.
**Ключевые идеи:** islice, filterfalse, dropwhile, takewhile, compress.

---

### 🔹 **Task 04 — Объединение последовательностей**

📂 `task04_chain_zip.py`
**Цель:** Комбинировать элементы из нескольких источников.
**Ключевые идеи:** chain, zip_longest.

---

### 🔹**Task 05 — Кумулятивные вычисления**

📂 `task05_accumulate_starmap.py`
**Цель:** Вычислить кумулятивные суммы и попарные суммы чисел.
**Ключевые идеи:** `accumulate`, `starmap(operator.add, ...)`, ленивые итераторы.

---

### 🔹**Task 06 — Pairwise / Tee**

📂 `task06_pairwise_tee.py`
**Цель:** Пройти по последовательности парами и создать независимые копии итератора.
**Ключевые идеи:** `pairwise`, `tee`, повторное потребление итераторов.

---

### 🔹**Task 07 — Группировка по ключу**

📂 `task07_groupby.py`
**Цель:** Сгруппировать отсортированные строки по первой букве.
**Ключевые идеи:** `sorted`, `groupby`, работа с группами.

---

### 🔹**Task 08 — Разбиение на батчи**

📂 `task08_batched.py`
**Цель:** Разбить поток чисел на пачки фиксированного размера.
**Ключевые идеи:** `batched`, ленивое потребление, `range`.


---

## 🔥 Дополнительная практика — задачи 09–16

Ниже — «боевые» задачи, имитирующие реальные сценарии потоковой обработки данных. Все решения строятся на идеях ленивых
итераторов и активно используют `itertools`.

### 🔹**Task 09 — Log Bursts Detector**

📂 `task09_log_bursts.py`

**Цель:** Найти «бурсты» подряд идущих ошибок 5xx в логах.
**Ключевые идеи:** `groupby`, ленивое чтение файла, `enumerate`.

---

### 🔹**Task 10 — Chunked Batches (ленивые чанки)**

📂 `task10_chunked_batches.py`
**Цель:** Разбить поток на пачки по `n` элементов.
**Ключевые идеи:** `islice`, собственный генератор `batched(iterable, n)`.

---

### 🔹**Task 11 — A/B-матрица с фильтрацией несовместимых**

📂 `task11_ab_matrix.py`
**Цель:** Сгенерировать конфигурации фич и отфильтровать запрещённые по правилам.
**Ключевые идеи:** `product`, потоковая фильтрация, ограничение вывода.

---

### 🔹**Task 12 — «Грязный» джойн CSV по позиции**

📂 `task12_zip_users.py`
**Цель:** Сопоставить `ids.csv` и `names.csv` построчно, дополняя короткую сторону.
**Ключевые идеи:** `zip_longest`, ленивое чтение файлов.

---

### 🔹**Task 13 — «Rolling Metric (скользящее среднее)**

📂 `task13_rolling_metric.py`
**Цель:** Считать среднее по окну размера `n` скользя по потоку.
**Ключевые идеи:** `deque(maxlen=n)`, при желании — `islice` для первичного окна.

---

### 🔹**Task 14 — Сессии пользователя по таймауту**

📂 `task14_sessionize.py`
**Цель:** Разбить события пользователя на сессии (разрыв > timeout → новая сессия).
**Ключевые идеи:** `groupby`, работа с `datetime`.

---

### 🔹**Task 15 — SKU-генератор**

📂 `task15_sku_generator.py`
**Цель:** Генерировать SKU-коды по шаблону `PREFIX-LLDD`.
**Ключевые идеи:** `product`, `islice` (для ограничения вывода).

---

### 🔹**Task 16 — Экспоненциальный backoff-расписание**

📂 `task16_backoff_schedule.py`
**Цель:** Сгенерировать ряд задержек ретраев: `base * 2^k`, с клиппингом до `max_delay`, и кумулятивом «время
наступления».
**Ключевые идеи:** бесконечный генератор, `islice` для ограничения, (опц.) `accumulate`.

## ▶️ Запуск

```bash
python task01_count_cycle_repeat.py
python task02_combinations.py
python task03_filter_slice.py
python task04_chain_zip.py
python task05_progression_stop.py
python task06_passwords.py
python task07_even_and_3.py
python task08_users_merge.py
python task09_log_bursts.py
python task10_chunked_batches.py
python task11_ab_matrix.py
python task12_zip_users.py
python task13_rolling_metric.py
python task14_sessionize.py
python task15_sku_gen.py
python task16_backoff_schedule.py
```

---

## 📁 Структура шага

```bash
step12_itertools/
├── data/
│   ├── ids.csv
│   ├── names.csv
│   ├── output.csv
│   └── sample.log
├── task01_count_cycle_repeat.py
├── task02_combinations.py
├── task03_filter_slice.py
├── task04_chain_zip.py
├── task05_progression_stop.py
├── task06_passwords.py
├── task07_even_and_3.py
├── task08_users_merge.py
├── task09_log_bursts.py
├── task10_chunked_batches.py
├── task11_ab_matrix.py
├── task12_zip_users.py
├── task13_rolling_metric.py
├── task14_sessionize.py
├── task15_sku_gen.py
├── task16_backoff_schedule.py
└── README.md
```

---

## 🛟 Устранение неполадок

| Проблема                                           | Причина                                       | Решение                                                                                 |
|----------------------------------------------------|-----------------------------------------------|-----------------------------------------------------------------------------------------|
| `ModuleNotFoundError: No module named 'itertools'` | Неверное окружение                            | Убедись, что используешь стандартный Python 3                                           |
| `StopIteration`                                    | Итератор закончился                           | Используй бесконечные генераторы (`count`, `cycle`) или проверяй длину                  |
| `MemoryError`                                      | Создание слишком больших списков из itertools | Используй `itertools` как ленивый итератор и не преобразуй в `list()` без необходимости |

---

## ✅ Критерии готовности

- [x] Все 4 задачи реализованы и протестированы
- [x] Используются соответствующие функции из `itertools`
- [x] Код корректно выводит данные и соответствует условиям
- [x] Нет отладочных принтов
- [x] Код отформатирован `black` и проходит `ruff`
- [x] В папке есть `README.md` с теорией, задачами, запуском и структурой
- [x] Все файлы названы `taskNN_name.py` и пронумерованы по порядку
