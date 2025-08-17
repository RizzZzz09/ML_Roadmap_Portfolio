# M1.4 — Функции в Python

## Теория

### 1. Что такое функция
Функция — это именованный блок кода, который можно вызывать многократно. Помогает:
- структурировать программу;
- избегать дублирования кода;
- делать код читаемее.
```python
def greet():
    print("Hello, world!")

greet()  # вызов функции
```

---

### 2. Аргументы функции
Функции могут принимать входные данные — аргументы.
```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

---

### 3. Возвращаемые значения (`return`)
Функция может возвращать результат.
```python
def add(a, b):
    return a + b

result = add(2, 3)
print(result)  # 5
```

---

### 4. Типы аргументов
**Позиционные**
```python
def power(base, exp):
    return base ** exp

print(power(2, 3))  # 8
```

**Именованные (keyword arguments)**
```python
print(power(exp=3, base=2))  # 8
```

**Аргументы по умолчанию**
```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()        # Hello, Guest
greet("Alice") # Hello, Alice
```

**Неограниченное количество аргументов**
- `*args` — собирает позиционные аргументы в кортеж.
- `**kwargs` — собирает именованные аргументы в словарь.
```python
def demo(*args, **kwargs):
    print(args)
    print(kwargs)

demo(1, 2, 3, name="Alice", age=25)
# (1, 2, 3)
# {'name': 'Alice', 'age': 25}
```

---

### 5. Область видимости (Scope)
Локальные переменные существуют только внутри функции.
Глобальные переменные доступны везде, но менять их внутри функции нельзя без `global`.
```python
x = 10  # глобальная переменная

def foo():
    y = 5  # локальная переменная
    print(x, y)

foo()      # 10 5
print(x)   # 10
# print(y)   # Ошибка! y вне области видимости
```

---

### 6. Возврат нескольких значений
Функция может возвращать несколько значений (на деле — кортеж).
```python
def get_person():
    return "Alice", 25

name, age = get_person()
print(name, age)  # Alice 25
```

---

### 7. Аннотации типов (typing)
Python поддерживает подсказки типов для аргументов и возвращаемого значения.
```python
def add(a: int, b: int) -> int:
    return a + b
```
Это не строгое правило, а лишь подсказка для IDE и линтеров.

---

### 8. Докстринги
У функции можно писать документацию (docstring).
```python
def add(a: int, b: int) -> int:
    """
    Складывает два числа.

    Args:
        a (int): Первое число
        b (int): Второе число

    Returns:
        int: Сумма чисел
    """
    return a + b
```

---

### 9. Лямбда-функции
Анонимные функции, которые удобно использовать для коротких операций.
```python
square = lambda x: x ** 2
print(square(4))  # 16
```
Часто применяются вместе с `map`, `filter`, `sorted`.

---

### 10. Рекурсия
Функция может вызывать саму себя. Пример: вычисление факториала.
```python
def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```
⚠️ Рекурсия должна иметь условие выхода, иначе программа уйдёт в бесконечный вызов.

---

### 11. Рекомендации (Best practices)
- Давай функциям говорящие имена.
- Делай функции маленькими (одна функция = одна логическая задача).
- Избегай слишком большого числа аргументов (>3–4).
- Пиши докстринги для важных функций.
- Старайся использовать аннотации типов.

---

## Задания

1. **Task 1 — Простая функция**
   Файл: `task1_greet.py`
   Написать функцию `greet()`, которая печатает `"Hello, world!"`.

2. **Task 2 — Аргументы функции**
   Файл: `task2_greet_name.py`
   Функция `greet(name)`, которая принимает имя и печатает приветствие.

3. **Task 3 — Возврат значения**
   Файл: `task3_add.py`
   Функция `add(a, b)` возвращает сумму двух чисел.

4. **Task 4 — Аргументы по умолчанию**
   Файл: `task4_greet_default.py`
   Функция `greet(name="Guest")`. Если имя не передано → `"Hello, Guest"`.

5. **Task 5 — *args и **kwargs**
   Файл: `task5_args_kwargs.py`
   Функция `demo(*args, **kwargs)` выводит список аргументов и словарь именованных аргументов.

6. **Task 6 — Область видимости**
   Файл: `task6_scope.py`
   Функция `foo()` выводит глобальную переменную и создаёт локальную. Попробовать вывести локальную вне функции.

7. **Task 7 — Возврат нескольких значений**
   Файл: `task7_multiple_return.py`
   Функция `get_person()` возвращает имя и возраст. Распаковать в две переменные.

8. **Task 8 — Аннотации типов**
   Файл: `task8_typing.py`
   Функция `multiply(a: int, b: int) -> int`, возвращающая произведение.

9. **Task 9 — Докстринги**
   Файл: `task9_docstring.py`
   Написать функцию `divide(a, b)`, добавить docstring в формате: `Args`, `Returns`, *(опционально)* `Raises` (если деление на 0).

10. **Task 10 — Лямбда-функции**
    Файл: `task10_lambda.py`
    Создать лямбда-функцию для возведения в квадрат. Применить её к списку чисел через `map`.

11. **Task 11 — Рекурсия**
    Файл: `task11_factorial_recursive.py`
    Функция `factorial(n)` с использованием рекурсии.

12. **Task 12 — Мини-челлендж**
    Файл: `task12_calculator.py`
    Сделать калькулятор с функциями: `add(a, b)`, `subtract(a, b)`, `multiply(a, b)`, `divide(a, b)` (с проверкой на 0). Программа должна спрашивать у пользователя числа и операцию.

---

## Запуск

```bash
python task1_greet.py
python task2_greet_name.py
python task3_add.py
python task4_greet_default.py
python task5_args_kwargs.py
python task6_scope.py
python task7_multiple_return.py
python task8_typing.py
python task9_docstring.py
python task10_lambda.py
python task11_factorial_recursive.py
python task12_calculator.py
```
