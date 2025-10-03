class NegativeNumberError(Exception):
    """Ошибка. Число не может быть меньше 0."""

    pass


def sqrt_strict():
    while True:
        number_input = input("Enter any positive number: ")
        if not number_input.lstrip("-").isdigit():
            raise ValueError("You did not enter a number")

        number = int(number_input)
        if number < 0:
            raise NegativeNumberError("This number is less than zero.")

        return number**0.5


if __name__ == "__main__":
    result = sqrt_strict()
    print(result)
