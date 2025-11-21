from typing import Any

MIN_PAYMENT = 100  # Минимальная сумма оплаты


class PaymentError(Exception):
    """Базовый класс ошибок при оплате."""

    pass


class PaymentInvalidValue(PaymentError):
    """Ошибка. Выбрасывается, если не удалось привести значение к int."""

    pass


class MinAmountViolation(PaymentError):
    """Ошибка. Выбрасывается, если число меньше указанного значения."""

    def __init__(self, amount: int, minimum: int):
        self.amount = amount
        self.minimum = minimum
        super().__init__(
            f"Минимальная сумма оплаты составляет {minimum}. Вы попытались оплатить {amount}."
        )


def charge_payment(amount: Any) -> bool:
    """
    Проверяет корректность оплаты. В случае успеха возвращает True.

    Args:
        amount (Any): оплата, переданная в функцию для обработки.

    Returns:
        bool: Результат оплаты.

    Raises:
        PaymentInvalidValue: Если не удалось привести amount к int.
        MinAmountViolation: Если amount < MIN_PAYMENT (MIN_PAYMENT = 100).
    """
    print(f'\nРаботает функция "{charge_payment.__name__}"')
    try:
        convert_to_int = int(amount)
    except ValueError as error:
        raise PaymentInvalidValue(f"Не удалось конвертировать {amount} в число.") from error

    if convert_to_int < MIN_PAYMENT:
        raise MinAmountViolation(convert_to_int, MIN_PAYMENT)

    return True


def main() -> None:
    print(f'Работает функция "{main.__name__}"')

    payment_input = input("Введите сумму для оплаты\n> ")
    try:
        charge_payment(payment_input)
    except PaymentInvalidValue as error:
        print(error, f"\n> {error.__cause__}")
    except MinAmountViolation as error:
        print(f"> {error}")
    else:
        print(f'\nРаботает функция "{main.__name__}"')
        print("Оплата прошла успешно.")


if __name__ == "__main__":
    main()
