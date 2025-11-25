from typing import Annotated, Union


class InvalidNumber(Exception):
    """Ошибка. Выбрасывается, если номер банковского счета пустая строка или состоит не из цифр."""

    pass


class InvalidBalance(Exception):
    """Ошибка. Выбрасывается, если баланс отрицательный."""


class BankAccount:
    def __init__(self, number: str, balance: Annotated[Union[int, float], "balance >= 0"]):
        if not number or not number.isdigit():
            raise InvalidNumber(
                f'Значение "number={number}" не может быть пустой строкой '
                f"и должно состоять только из цифр."
            )

        if not isinstance(balance, (int, float)) or balance < 0:
            raise InvalidBalance(
                f'Значение "balance={balance}:{type(balance).__name__}" '
                f"должно быть положительным числом или равно 0."
            )

        self._number = number
        self._balance = balance

    @property
    def number(self) -> str:
        return self._number

    @property
    def balance(self) -> Union[int, float]:
        return self._balance

    @balance.setter
    def balance(self, value: Union[int, float]) -> None:
        if not isinstance(value, (int, float)) or value < 0:
            raise InvalidBalance(
                f'Значение "balance={value}:{type(value).__name__}" '
                f"должно быть положительным числом или равно 0."
            )
        self._balance = value

    @property
    def is_empty(self) -> bool:
        return self.balance == 0

    def __repr__(self) -> str:
        return f"BankAccount(number={self.number!r}, balance={self.balance})"

    def __str__(self) -> str:
        return f"Your bank account: number: {self.number}, balance: {self.balance}"


def main() -> None:
    number = "123456789"
    balance = 1000

    try:
        bank_account = BankAccount(number, balance)
    except (InvalidNumber, InvalidBalance) as error:
        print(f"> {error}")
    else:
        print(bank_account.is_empty)
        print(bank_account)
        print(repr(bank_account))


if __name__ == "__main__":
    main()
