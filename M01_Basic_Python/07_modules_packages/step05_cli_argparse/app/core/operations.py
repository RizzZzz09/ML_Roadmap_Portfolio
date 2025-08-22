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
