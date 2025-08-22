# M1.5 — Comprehensions и генераторы в Python

## 📘 Теория — M1.5 Comprehensions и генераторы

1) **List comprehensions (генераторы списков)** — короткая запись циклов для создания списков.
Вместо:
```python
squares = []
for x in range(5):
    squares.append(x**2)
```
Можно написать:
```python
squares = [x**2 for x in range(5)]
```
Особенности: условие и вложенные циклы:
```python
evens = [x for x in range(10) if x % 2 == 0]
pairs = [(x, y) for x in range(3) for y in range(2)]
```

2) **Set comprehensions (множества)** — тот же синтаксис, фигурные скобки:
```python
unique_letters = {c for c in "hello world"}
```

3) **Dict comprehensions (словари)** — построение словаря:
```python
squares = {x: x**2 for x in range(5)}
```

4) **Условные выражения внутри comprehensions**:
```python
labels = ["even" if x % 2 == 0 else "odd" for x in range(6)]
```

5) **Генераторы (generator expressions)** — как list comp, но круглые скобки и ленивое вычисление:
```python
squares_gen = (x**2 for x in range(5))
print(next(squares_gen))  # 0
print(next(squares_gen))  # 1
```

6) **Функции‑генераторы (`yield`)** — обычная функция с `yield` вместо `return`.
```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(5):
    print(i)
```
`return` завершает функцию, `yield` «замораживает» состояние и продолжает позже.

7) **Генератор Фибоначчи**:
```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
```

8) **Сравнение памяти**:
```python
import sys
lst = [x**2 for x in range(1_000_000)]
gen = (x**2 for x in range(1_000_000))
print(sys.getsizeof(lst))  # ~МБ
print(sys.getsizeof(gen))  # ~сотни байт
```

⚡ **Итого**:
Comprehensions — быстрый способ создавать коллекции.
Генераторы — ленивость, экономия памяти, удобство бесконечных последовательностей.

---

## 🧭 Мини‑итог
- Comprehensions — декларативное построение коллекций (списки/множества/словари) с условиями и вложенностями.
- Generator expression и `yield` — ленивость и бережная память.
- Прикладные задачи: фильтрация/нормализация, батчи/семплинг, токены/частоты, мини‑EDA.

---

## 🧪 Практика — задачи

### Базовый блок (Tasks 1–9)

1. **Task 1 — Квадраты чисел** — `task1_squares.py`
2. **Task 2 — Чётные числа** — `task2_evens.py`
3. **Task 3 — Уникальные буквы** — `task3_unique_letters.py`
4. **Task 4 — Частотный словарь (список слов)** — `task4_word_freq.py`
5. **Task 5 — Таблица координат (вложенный comp)** — `task5_coordinates.py`
6. **Task 6 — Метки чётности (тернарка)** — `task6_labels.py`
7. **Task 7 — Генератор Фибоначчи (`yield`)** — `task7_fibonacci.py`
8. **Task 8 — Память: список vs генератор** — `task8_memory_compare.py`
9. **Task 9 — Бесконечный генератор чётных** — `task9_infinite_evens.py`
---
### Дополнительный блок — ближе к ML (Tasks 10–17)
10. **Task 10 — Фильтрация данных (температуры)** — `task10_filter_data.py`
11. **Task 11 — Частотность слов (NLP mini)** — `task11_word_freq_text.py`
12. **Task 12 — Уникальные пользователи (логи)** — `task12_unique_users.py`
13. **Task 13 — Нормализация данных** — `task13_normalization.py`
14. **Task 14 — Генератор батчей (mini‑DataLoader)** — `task14_batches.py`
15. **Task 15 — Random sampler** — `task15_random_samples.py`
16. **Task 16 — Словарь статистик (mini‑EDA)** — `task16_stats.py`
17. **Task 17 — Генератор токенов (NLP)** — `task17_tokens.py`

---

## ▶️ Запуск (быстрый список)

```bash
python task01_squares.py
python task02_evens.py
python task03_unique_letters.py
python task04_word_freq.py
python task05_coordinates.py
python task06_labels.py
python task07_fibonacci.py
python task08_memory_compare.py
python task09_infinite_evens.py

python task10_filter_data.py
python task11_word_freq_text.py
python task12_unique_users.py
python task13_normalization.py
python task14_batches.py
python task15_random_samples.py
python task16_stats.py
python task17_tokens.py
```
