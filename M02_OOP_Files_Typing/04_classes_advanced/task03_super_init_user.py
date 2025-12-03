class InvalidUsername(Exception):
    """Ошибка. Выбрасывается, когда имя пользователя пустая строка."""


class InvalidEmail(Exception):
    """Ошибка. Выбрасывается, когда введен неверный формат для почты ли строка с почтой пустая."""


class InvalidAccessLevel(Exception):
    """Ошибка. Возникает когда уровень доступа не целое число от 1 до 10."""

    pass


class User:
    def __init__(self, username: str, email: str):
        if not username:
            raise InvalidUsername("Имя пользователя не может быть пустой строкой.")

        if not email or email.find("@") == -1:
            raise InvalidEmail(f"Введена некорректная электронная почта: {email}.")

        self._username = username
        self._email = email

    @property
    def username(self) -> str:
        return self._username

    @property
    def email(self) -> str:
        return self._email

    def info(self) -> str:
        return f"User {self.username} ({self.email})"


class Admin(User):
    def __init__(self, username: str, email: str, access_level: int):
        if not isinstance(access_level, int) or access_level < 1 or access_level > 10:
            raise InvalidAccessLevel("Допустимое значение для уровня доступа число от 1 до 10.")

        super().__init__(username, email)

        self._access_level = access_level

    @property
    def access_level(self) -> int:
        return self._access_level

    def info(self) -> str:
        return f"Admin {self.username} ({self.email}) [level={self.access_level}]"


def main() -> None:
    username = "RizzZzz123456789"
    email = "abc@gmail.com"

    try:
        user = User(username, email)
        admin = Admin(username, email, 1)
    except (InvalidUsername, InvalidEmail, InvalidAccessLevel) as error:
        print(f"> {error}")
    else:
        print(user.info())
        print(admin.info())


if __name__ == "__main__":
    main()
