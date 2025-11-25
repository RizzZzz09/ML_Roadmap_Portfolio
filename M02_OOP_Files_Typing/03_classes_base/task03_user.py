from typing import Annotated


class InvalidUserName(Exception):
    """Ошибка. Выбрасывается, если имя пользователя пустая строка."""

    pass


class InvalidAge(Exception):
    """Ошибка. Выбрасывается, если значение возраста меньше или равно 0, или не целое число."""

    pass


class User:
    def __init__(self, username: str, age: Annotated[int, "age>0"]):
        if not username.strip():
            raise InvalidUserName("Имя пользователя не может быть пустой строкой.")
        if not isinstance(age, int) or age <= 0:
            raise InvalidAge("Значение возраста может быть только положительным целым числом.")

        self._username: str = username
        self._age: Annotated[int, "age>0"] = age

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, value: str) -> None:
        if not value.strip():
            raise InvalidUserName("Имя пользователя не может быть пустой строкой.")
        self._username = value

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: Annotated[int, "age>0"]) -> None:
        if not isinstance(value, int) or value <= 0:
            raise InvalidAge("Значение возраста может быть только положительным целым числом.")
        self._age = value

    @property
    def full_name(self) -> str:
        return f"{self.username} - {self.age}"

    def __repr__(self) -> str:
        return f"User(username={self.username!r}, age={self.age})"

    def __str__(self) -> str:
        return f"{self.username}, {self.age} y.o."


def main() -> None:
    user_name = "Danil"
    age = 24

    try:
        user = User(user_name, age)
    except (InvalidUserName, InvalidAge) as error:
        print(f"> {error}")
    else:
        print(user.full_name)
        print(user)
        print(repr(user))


if __name__ == "__main__":
    main()
