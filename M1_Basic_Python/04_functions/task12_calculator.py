def add(a: float, b: float) -> float:
    """
    Складывает числа a и b.

    Args:
        a (float): Первое число.
        b (float): Второе число.

    Returns:
        float: Результат сложения.
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Отнимает от числа a число b.

    Args:
        a (float): Первое число.
        b (float): Второе число.

    Returns:
        float: Результат вычитания.
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Умножает число a на b.

    Args:
        a (float): Первое число.
        b (float): Второе число.

    Returns:
        float: Результат умножения.
    """
    return a * b


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


def main():
    """Точка входа калькулятора."""
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    operation = input('Enter the operation "+", "-", "*" or "/": ').strip()

    match operation:
        case "+":
            result = add(first_number, second_number)
            print(f"Result: {result}")
        case "-":
            result = subtract(first_number, second_number)
            print(f"Result: {result}")
        case "*":
            result = multiply(first_number, second_number)
            print(f"Result: {result}")
        case "/":
            if second_number == 0:
                print("Division by zero is not allowed")
                return
            result = divide(first_number, second_number)
            print(f"Result: {result}")
        case _:
            print("Unknown operation")


if __name__ == "__main__":
    main()
