# M1.7 — Modules & Packages
## Step 10 — Дополнительные структуры данных (`collections`)

## 📘 Теория — Модуль `collections`

Модуль `collections` — часть стандартной библиотеки Python, предоставляющая **расширенные структуры данных**, которые
упрощают и ускоряют работу с данными.

---

### `namedtuple`

Именованные кортежи — как обычные `tuple`, но с полями по именам.

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y)  # 3 4
```

🔹 Неизменяемы
🔹 Доступ по имени и индексу
🔹 Удобны для компактных структур (координаты, студенты и т.д.)

---

### `deque` — двусторонняя очередь

Быстрая очередь с возможностью добавления и удаления с обоих концов за `O(1)`.

```python
from collections import deque

dq = deque([1, 2, 3])
dq.append(4)
dq.appendleft(0)
dq.pop()
dq.popleft()
dq.rotate(2)
```

🔹 `append`, `appendleft`, `pop`, `popleft`, `rotate`, `clear`
🔹 Используется для очередей, буферов, симуляций обслуживания

---

### `Counter` — счётчик

Подсчёт количества вхождений объектов.

```python
from collections import Counter

c = Counter("abracadabra")
print(c.most_common(3))  # [('a', 5), ('b', 2), ('r', 2)]
```

🔹 `+`, `-`, `&`, `|` для арифметики
🔹 Удобен для подсчёта символов, слов, событий

---

### `defaultdict` — словарь с значением по умолчанию

Автоматически создаёт пустое значение, если ключа ещё нет.

```python
from collections import defaultdict

d = defaultdict(list)
d["a"].append(1)
```

🔹 `list`, `int`, `set` как фабрики
🔹 Используется для группировок, индексов, агрегаций

---

### `OrderedDict` — упорядоченный словарь

Сохраняет порядок вставки ключей и позволяет им управлять.

```python
from collections import OrderedDict

od = OrderedDict()
od["a"] = 1
od["b"] = 2
od.move_to_end("a")
od.popitem(last=False)
```

🔹 `move_to_end`, `popitem(last=...)`
🔹 Полезен для LRU-кэшей, истории действий

---

### `ChainMap` — объединение словарей

Объединяет несколько словарей в один видимый.

```python
from collections import ChainMap

system = {"theme": "light", "lang": "en"}
env = {"lang": "lv"}
user = {"theme": "dark"}

settings = ChainMap(user, env, system)
print(settings["theme"])  # dark
```

🔹 Поиск слева направо: user > env > system
🔹 Удобен для конфигов

---

## 🧪 Практика — задачи

🔹 **Task 01 — Point distance**
📂 `task01_point_distance.py`
Создай `Point(x, y)` через `namedtuple`. Вычисли расстояние между двумя точками по формуле Евклида.

🔹 **Task 02 — Students journal**
📂 `task02_students_journal.py`
Создай `Student(name, grade, subject)`. Отфильтруй по предмету и выведи топ-3 по оценке.

🔹 **Task 03 — Service queue**
📂 `task03_service_queue.py`
Симулируй очередь (`deque`) с командами `ARRIVE`, `SERVE`, `PEEK`, `SIZE`, `END`.

🔹 **Task 04 — Rotate and sliding window**
📂 `task04_rotate_and_window.py`
Реализуй циклический сдвиг (`rotate`) и поиск максимумов в окне шириной `w`.

🔹 **Task 05 — Char frequencies**
📂 `task05_char_freq.py`
Подсчитай частоты символов через `Counter` и выведи топ-5.

🔹 **Task 06 — Word stats**
📂 `task06_word_stats.py`
Подсчитай частоты слов в двух текстах, выведи union / intersection / уникальные для первого.

🔹 **Task 07 — OrderedDict ops**
📂 `task07_ordered_ops.py`
Управляй порядком элементов в `OrderedDict`: `move_to_end`, `popitem`, `show`.

🔹 **Task 08 — Grouping by department**
📂 `task08_grouping_defaultdict.py`
Группировка имён по департаментам и средние зарплаты (`defaultdict`).

🔹 **Task 09 — Prefix index**
📂 `task09_prefix_index.py`
Индекс слов по первой букве (`defaultdict(list)`), сортировка внутри каждой буквы.

🔹 **Task 10 — Config merge**
📂 `task10_chainmap_config.py`
Объединение `user/env/system` настроек с приоритетами через `ChainMap`.

🔹 **Task 11 — Word sampling**
📂 `task11_counter_sampling.py`
Построй `Counter`, сформируй `population` и `weights`, сделай 10 000 выборок и сравни частоты.

🔹 **Task 12 — LRU cache simulation**
📂 `task12_lru_cache_sim.py`
Реализуй LRU-кеш на `OrderedDict` с командами `cap`, `put`, `get`, `show`.

---

## ▶️ Запуск

```bash
python task01_point_distance.py
python task02_students_journal.py
python task03_service_queue.py
python task04_rotate_and_window.py
python task05_char_freq.py
python task06_word_stats.py
python task07_ordered_ops.py
python task08_grouping_defaultdict.py
python task09_prefix_index.py
python task10_chainmap_config.py
python task11_counter_sampling.py
python task12_lru_cache_sim.py
```


## 📁 Структура шага
_(добавить дерево файлов)_


## 🛟 Устранение неполадок
_(добавить частые ошибки)_


## ✅ Критерии готовности
_(добавить чеклист)_
