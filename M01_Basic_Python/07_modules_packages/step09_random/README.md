# M1.7 — Modules & Packages
## Step 09 — Генерация случайностей (`random`)

## 🎯 Цель шага
Познакомиться с возможностями модуля `random` для генерации случайных чисел, работы с последовательностями и моделирования случайных процессов.

---

## 📘 Теория

### ⚙️ Общие принципы
- Модуль `random` — генератор **псевдослучайных** чисел (PRNG) на основе **Mersenne Twister**.
- Детерминированный: при одинаковом `seed` выдаёт одинаковую последовательность.
- ⚠️ Не использовать для безопасности (для этого есть `secrets`).

---

### 🎲 Управление генератором
```python
random.seed(42)           # фиксируем начальное состояние
state = random.getstate() # сохраняем внутреннее состояние
random.setstate(state)    # восстанавливаем состояние
```

---

### 🔢 Генерация чисел
| Функция                  | Описание                              |
|---------------------------|------------------------------------------|
| `random.random()`         | float ∈ [0.0, 1.0)                        |
| `random.uniform(a, b)`    | float ∈ [a, b]                            |
| `random.randint(a, b)`    | целое ∈ [a, b]                            |
| `random.randrange(start, stop, step)` | целое как `range`            |

---

### 📋 Работа с последовательностями
| Функция                                   | Описание                               |
|---------------------------------------------|-------------------------------------------|
| `random.choice(seq)`                        | 1 элемент                                 |
| `random.choices(seq, k, weights=...)`       | выборка с возвращением (дубликаты)         |
| `random.sample(seq, k)`                     | выборка без возвращения (уникальные)       |
| `random.shuffle(seq)`                       | перемешивает список **на месте**           |

---

### 📈 Распределения
- `random.gauss(mu, sigma)` / `normalvariate(...)` — нормальное распределение
- `random.expovariate(lambd)` — экспоненциальное (среднее = 1/λ)
- `random.triangular(low, high, mode)` — треугольное
- (есть и другие: lognorm, gamma, beta, weibull…)

---

### ⚡ Важные нюансы
- `random` не криптостойкий → для токенов/паролей: `secrets`.
- `shuffle` меняет список на месте, не возвращает новый.
- `choices` может выдавать дубликаты, `sample` — нет.
- `seed` нужно ставить **один раз** перед генерацией, а не в цикле.

---

## 💥 Челлендж
📂 `task13_queue_simulation.py`

Симуляция очереди:
- клиенты приходят по экспоненциальному закону (`expovariate`),
- время обслуживания нормально распределено (`gauss`),
- один сервер, работа по очереди,
- считаем: среднее ожидание, среднее обслуживание, среднюю длину очереди.

---

## 🧪 Практика — задачи

🔹 **Task 01 — Seed repeat**
📂 `task01_seed_repeat.py`
Демонстрация повторяемости случайных чисел при фиксированном seed.

🔹 **Task 02 — Dice**
📂 `task02_dice.py`
Симуляция 20 бросков кубика, подсчёт количества выпадений каждой грани.

🔹 **Task 03 — Uniform**
📂 `task03_uniform.py`
Генерация 10 случайных чисел с равномерным распределением от -1 до 1.

🔹 **Task 04 — Fruits**
📂 `task04_fruits.py`
Выбор случайных фруктов: один choice, 5 с возвращением choices, 2 без возвращения sample.

🔹 **Task 05 — Shuffle**
📂 `task05_shuffle.py`
Перемешивание списка чисел с помощью shuffle.

🔹 **Task 06 — Passwords**
📂 `task06_passwords.py`
Генерация пароля и объяснение, почему для безопасности нужно использовать secrets.

🔹 **Task 07 — Weighted lottery**
📂 `task07_weighted_lottery.py`
Лотерея с весами и сравнение эмпирических и ожидаемых вероятностей.

🔹 **Task 08 — Monte Carlo π**
📂 `task08_monte_carlo_pi.py`
Оценка числа π методом Монте-Карло.

🔹 **Task 09 — State roundtrip**
📂 `task09_state_roundtrip.py`
Сохранение и восстановление состояния генератора.

🔹 **Task 10 — Randrange grid**
📂 `task10_randrange_grid.py`
Случайная точка на сетке 0..95 с шагом 5.

🔹 **Task 11 — Bootstrap mean**
📂 `task11_bootstrap_mean.py`
Бутстрэп-оценка доверительного интервала среднего.

🔹 **Task 12 — Triangular estimation**
📂 `task12_triangular_estimation.py`
Оценка вероятности уложиться в срок по треугольному распределению.

---

## Запуск

```bash
python task01_seed_repeat.py
python task02_dice.py
python task03_uniform.py
python task04_fruits.py
python task05_shuffle.py
python task06_passwords.py
python task07_weighted_lottery.py
python task08_monte_carlo_pi.py
python task09_state_roundtrip.py
python task10_randrange_grid.py
python task11_bootstrap_mean.py
python task12_triangular_estimation.py
python task13_queue_simulation.py
```

---

## ✅ Критерии готовности
- Понимание `seed`, `state`, `random.*`
- Работа с выборками и весами
- Моделирование случайных процессов
- Подготовка к `collections.Counter` (Step 10)


## 📁 Структура шага
_(добавить дерево файлов)_


## 🛟 Устранение неполадок
_(добавить частые ошибки)_
