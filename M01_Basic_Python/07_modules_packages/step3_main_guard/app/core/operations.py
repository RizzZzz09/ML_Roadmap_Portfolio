def add(a: float, b: float) -> float:
    """
    Возвращает сумму чисел a и b.

    Args:
        a (float): Первое слагаемое.
        b (float): Второе слагаемое.

    Returns:
        float: Результат сложения.
    """
    return a + b


def sub(a: float, b: float) -> float:
    """
    Возвращает разницу чисел a и b.

    Args:
        a (float): Уменьшаемое.
        b (float): Вычитаемое.

    Returns:
        float: Разница.
    """
    return a - b


def mul(a: float, b: float) -> float:
    """
    Возвращает произведение чисел a и b.

    Args:
        a (float): Первый множитель.
        b (float): Второй множитель.

    Returns:
        float: Произведение.
    """
    return a * b


def div(a: float, b: float) -> float | str:
    """
    Возвращает частное чисел a и b.

    Args:
        a (float): Делимое.
        b (float): Делитель.

    Returns:
        float: Частное.
        str: Текст ошибки при делении на 0.
    """
    if b == 0:
        return "Division by zero is not allowed"
    return a / b


def add_list(first_list: list[int | float], second_list: list[int | float]) -> list[int | float]:
    """
    Возвращает список суммы элементов двух списков по индексу.
    При разной длине списков "хвост" списка, который длиннее добавляется в результат.

    Args:
        first_list: Первый список.
        second_list: Второй список.

    Returns:
        list[int | float]: Список суммы элементов двух списков.
    """
    min_length = min(len(first_list), len(second_list))
    result = []

    for i in range(min_length):
        result.append(add(first_list[i], second_list[i]))

    if len(first_list) > len(second_list):
        result.extend(first_list[min_length:])
    else:
        result.extend(second_list[min_length:])

    return result


print("__name__ in operations:", __name__)
