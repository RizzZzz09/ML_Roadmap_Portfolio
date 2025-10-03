class OperationNotSupportedError(Exception):
    """Ошибка о неизвестной операции."""

    pass


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


def div(a: float, b: float) -> float:
    """
    Возвращает частное чисел a и b.

    Args:
        a (float): Делимое.
        b (float): Делитель.

    Returns:
        float: Частное.

    Raises:
        ZeroDivisionError: Если число 'b' равно 0.
    """
    try:
        return a / b
    except ZeroDivisionError:
        raise


def parser(number: str) -> float:
    """
    Преобразовывает строку в число с плавающей точкой.

    Args:
        number (str): Строка, которую нужно преобразовать в число с плавающей точкой.

    Returns:
        float: Результат преобразования строки.

    Raises:
        ValueError: Если 'number' не число.
    """
    try:
        return float(number)
    except ValueError as error:
        raise ValueError("You must enter a valid number") from error


def read_two_floats() -> tuple[float, float]:
    """
    Запрашивает у пользователя первое число и второе число для преобразования в float.

    Returns:
        tuple(float, float): Кортеж преобразованных чисел.

    """
    a = parser(input("Enter first number: ").strip())
    b = parser(input("Enter second number: ").strip())
    return a, b


def main():
    while True:
        try:
            user_input = (
                input("Enter operation (add, sub, mul, div) or q to exit: ").lower().strip()
            )
            if user_input == "q":
                print("THE PROGRAM IS COMPLETED")
                break

            match user_input:
                case "add":
                    first_number, second_number = read_two_floats()
                    print(f"Result: {add(first_number, second_number)}\n")
                case "sub":
                    first_number, second_number = read_two_floats()
                    print(f"Result: {sub(first_number, second_number)}\n")
                case "mul":
                    first_number, second_number = read_two_floats()
                    print(f"Result: {mul(first_number, second_number)}\n")
                case "div":
                    first_number, second_number = read_two_floats()
                    print(f"Result: {div(first_number, second_number)}\n")
                case _:
                    raise OperationNotSupportedError(user_input)
        except ValueError as e:
            print(f"You must enter only numbers: {e}\n")
        except ZeroDivisionError as e:
            print(f"You can't divide by zero: {e}\n")
        except OperationNotSupportedError as e:
            print(f"Unknown operation: {e}. Use: add, sub, mul, div.\n")
            continue


if __name__ == "__main__":
    main()
