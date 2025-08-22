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
