# M1.3 — Циклы в Python

## Теория

### 1. Цикл `for`
Используется, когда нужно выполнить блок кода фиксированное количество раз или пройти по элементам последовательности.
```python
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4
```

---

### 2. Цикл `while`
Выполняется, пока условие истинно.
```python
x = 0
while x < 5:
    print(x)
    x += 1
```

---

### 3. Управляющие операторы
- `break` — прерывает цикл полностью.
- `continue` — переходит к следующей итерации.
- `else` — выполняется, если цикл завершился **без `break`**.

```python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "=", x, "*", n//x)
            break
    else:
        print(n, "— простое число")
```

---

### 4. Вложенные циклы
Цикл внутри цикла.
```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

---

### 5. Функция `enumerate`
Позволяет одновременно получить индекс и элемент.
```python
for index, char in enumerate("Cat"):
    print(index, char)
```

---

### 6. Функция `zip`
Объединяет несколько последовательностей в кортежи.
```python
names = ["Alice", "Bob"]
ages = [25, 30]
for name, age in zip(names, ages):
    print(name, age)
```

---

### 7. List Comprehensions
Краткая форма записи циклов для генерации списков.
```python
squares = [x ** 2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]
```

---

### 8. Рекомендации
- Используй `for`, если известно количество итераций.
- Используй `while`, если количество итераций заранее не известно.
- `break` и `continue` применяй осознанно.
- `enumerate` и `zip` делают код чище, чем работа с индексами вручную.
- List comprehensions полезны для лаконичного кода, но избегай слишком сложных выражений.

---

## Задания

1. **Сумма чисел**
   Ввод: `N`.
   Вывод: сумма чисел от 1 до `N`.

2. **Факториал**
   Ввод: `N`.
   Вывод: произведение чисел от 1 до `N`.

3. **Таблица умножения**
   Ввод: число.
   Вывод: таблица умножения до 10.

4. **Разворот строки**
   Ввод: строка.
   Вывод: строка в обратном порядке.

5. **Проверка числа на простоту**
   Ввод: число.
   Вывод: "Prime" или "Not prime".

6. **Пропуск чётных чисел**
   Ввод: `N`.
   Вывод: все нечётные числа от 1 до `N`.

7. **Вложенные циклы**
   Ввод: `N`.
   Вывод: квадрат `N × N` из `*`.

8. **enumerate**
   Ввод: строка.
   Вывод: символы с индексами.

9. **zip**
   Использовать `zip` для объединения двух списков (например, имена и возраст).

10. **List comprehension**
    Создать список квадратов чисел от 1 до 10.

---

## Запуск

```bash
python task1_sum.py
python task2_factorial.py
python task3_multiplication_table.py
python task4_reverse_string.py
python task5_prime.py
python task6_skip_even.py
python task7_square_stars.py
python task8_enumerate.py
python task9_zip_lists.py
python task10_list_comprehension.py
```
