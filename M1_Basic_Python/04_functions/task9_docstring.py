def divide(a: float, b: float) -> float:
    """
    Делит число a на b.

    Args:
        a (float): Первое число.
        b (float): Второе число.

    Returns:
        float: Результат деления.
    """
    return a / b


if __name__ == "__main__":
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    result = divide(first_number, second_number)
    print(f"Result: {result}")
