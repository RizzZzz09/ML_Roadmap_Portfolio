# M1.5 — Коллекции в Python

## 📘 Теория — Коллекции в Python

### 1. Общая идея
Коллекции — это структуры данных, позволяющие хранить наборы элементов.
В Python есть встроенные универсальные коллекции:

- **list** — список (изменяемый, упорядоченный)
- **tuple** — кортеж (неизменяемый, упорядоченный)
- **set** — множество (уникальные элементы, порядок не гарантируется)
- **dict** — словарь (ключ-значение, изменяемый, начиная с Python 3.7 — упорядоченный по вставке)

---

### 2. Списки (`list`)
Изменяемая последовательность.

Индексация и срезы, допускаются разные типы в одном списке.

Пример:
```python
nums = [1, 2, 3, 4]
print(nums[0])      # 1
print(nums[-1])     # 4
print(nums[1:3])    # [2, 3]

nums.append(5)      # добавление
nums.remove(2)      # удалить первое вхождение
nums.pop()          # удалить последний и вернуть его
nums.insert(1, 10)  # вставить на позицию
nums.sort()         # сортировать
nums.reverse()      # развернуть
```

⚡ Методы: `.append()`, `.extend()`, `.insert()`, `.remove()`, `.pop()`, `.index()`, `.count()`, `.sort()`, `.reverse()`, `.clear()`

---

### 3. Кортежи (`tuple`)
Неизменяемая версия списка.

Используются для хранения фиксированных наборов значений.

Лёгкие по памяти и быстрее списков.

```python
point = (10, 20)
x, y = point  # распаковка
print(x, y)
```

Особенность: если нужен кортеж из одного элемента → `(42,)` (иначе это будет просто число в скобках).

---

### 4. Множества (`set`, `frozenset`)
Хранят только **уникальные элементы**.

Операции как в математике: объединение, пересечение, разность.
```python
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)   # {1, 2, 3, 4, 5} (объединение)
print(a & b)   # {3} (пересечение)
print(a - b)   # {1, 2} (разность)
print(a ^ b)   # {1, 2, 4, 5} (симметрическая разность)
```

Методы: `.add()`, `.remove()`, `.discard()`, `.pop()`, `.clear()`, `.update()`
`frozenset` — неизменяемое множество.

---

### 5. Словари (`dict`)
Хранят пары «ключ → значение».

Ключи должны быть **хешируемыми** (например, числа, строки, кортежи).

```python
person = {"name": "Alice", "age": 25}
print(person["name"])       # Alice
person["city"] = "Riga"     # добавление
print(person.get("email"))  # None (без ошибки)

for key, value in person.items():
    print(key, value)
```

Методы: `.keys()`, `.values()`, `.items()`, `.get()`, `.update()`, `.pop()`, `.popitem()`, `.clear()`

---

### 6. Вложенные коллекции
Можно хранить коллекции внутри коллекций:
```python
matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix[1][0])  # 3

users = [
    {"name": "Danil", "age": 20},
    {"name": "Alice", "age": 25},
]
```

---

### 7. Операции над коллекциями
- `len(x)` — длина
- `in` — проверка наличия
- `sum()`, `min()`, `max()` для числовых коллекций
- `sorted(iterable)` возвращает новый отсортированный список
- `enumerate()` для индексации в цикле

```python
nums = [10, 20, 30]
for i, val in enumerate(nums):
    print(i, val)
```

---

### 8. Распаковка коллекций
```python
a, b, c = [1, 2, 3]
print(a, b, c)   # 1 2 3

x, *rest = [1, 2, 3, 4, 5]
print(x, rest)   # 1 [2, 3, 4, 5]
```

---

### 9. Генераторы коллекций (comprehensions — будет в следующей теме, но зацепим)
Краткая форма записи:
```python
squares = [x**2 for x in range(5)]
evens = {x for x in range(10) if x % 2 == 0}
dict_example = {x: x**2 for x in range(5)}
```

---

### 10. Где какие коллекции применять
- **list** — универсальный изменяемый контейнер.
- **tuple** — для фиксированных структур, «запакованных» значений (координаты, возвращение нескольких значений).
- **set** — для уникальности и быстрой проверки принадлежности.
- **dict** — для ассоциативного хранения (ключ → значение).

---

## 📝 Мини-итог
- **list** — изменяемый массив.
- **tuple** — неизменяемый список.
- **set** — уникальные значения, операции множеств.
- **dict** — пары ключ-значение, быстрый доступ.
- Все коллекции поддерживают итерацию, распаковку, встроенные функции (`len`, `sorted`, `enumerate`).
- Выбор коллекции зависит от задачи: нужны ли уникальные элементы, порядок, изменяемость.

---

## 🧪 Практика — задачи

1. **Task 1 — Индексация и срезы** — `task1_slices.py`
2. **Task 2 — Методы списка** — `task2_list_methods.py`
3. **Task 3 — Подсчёт элементов** — `task3_word_count.py`
4. **Task 4 — Уникальные элементы (merge без дубликатов)** — `task4_unique_merge.py`
5. **Task 5 — Кортежи (max и медиана)** — `task5_tuple_max.py`
6. **Task 6 — Преобразование в хэшируемое** — `task6_tuple_key.py`
7. **Task 7 — Множества: домены из email** — `task7_set_domains.py`
8. **Task 8 — Операции множеств** — `task8_set_operations.py`
9. **Task 9 — Словарь из пар (суммы по ключам)** — `task9_dict_from_pairs.py`
10. **Task 10 — Безопасный доступ к словарю** — `task10_dict_safe_get.py`
11. **Task 11 — Частоты символов** — `task11_char_freq.py`
12. **Task 12 — Инвертирование словаря** — `task12_dict_invert.py`
13. **Task 13 — Группировка по категории** — `task13_grouping.py`
14. **Task 14 — Объединение словарей** — `task14_dict_merge.py`
15. **Task 15 — Нормализация цен** — `task15_normalize_prices.py`
16. **Task 16 — Уникальные пары (без зеркал)** — `task16_unique_pairs.py`
17. **Task 17 — Фильтр по стоп-словам** — `task17_filter_stopwords.py`
18. **Task 18 — Топ-N элементов** — `task18_top_n.py`
19. **Task 19 — Объединение списков пользователей по id** — `task19_merge_users.py`
20. **Task 20 — Число уникальных слов** — `task20_unique_words.py`
21. **Task 21 — Челлендж: Анализ текста** — `task21_text_analysis.py`

---

## ▶️ Запуск
Из данной директории:
```bash
python task1_slices.py
python task2_list_methods.py
python task3_word_count.py
python task4_unique_merge.py
python task5_tuple_max.py
python task6_tuple_key.py
python task7_set_domains.py
python task8_set_operations.py
python task9_dict_from_pairs.py
python task10_dict_safe_get.py
python task11_char_freq.py
python task12_dict_invert.py
python task13_grouping.py
python task14_dict_merge.py
python task15_normalize_prices.py
python task16_unique_pairs.py
python task17_filter_stopwords.py
python task18_top_n.py
python task19_merge_users.py
python task20_unique_words.py
python task21_text_analysis.py
```
