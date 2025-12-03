class InvalidAge(Exception):
    """Ошибка. Выбрасывается, если возраст пользователя не целое или отрицательное число."""

    pass


class InvalidUsername(Exception):
    """Ошибка. Выбрасывается, если имя пользователя пустое или состоит не только из букв и цифр."""

    pass


class Profile:
    def __init__(self, age: int, bio: str):
        if not isinstance(age, int) or age <= 0:
            raise InvalidAge(
                f'Значение возраста "{age}" может быть только положительным целым числом.'
            )

        self._age = age
        self._bio = bio

    @property
    def age(self) -> int:
        return self._age

    @property
    def bio(self) -> str:
        return self._bio

    def short(self) -> str:
        return f"age={self.age}, bio={self.bio}"


class User:
    def __init__(self, username: str, profile: Profile):
        if not username or not username.isalnum():
            raise InvalidUsername(
                f'Имя пользователя: "{username}" невалидно.'
                f"\nИмя пользователя не может быть пустой строкой"
                f" и должно состоять только из букв и цифр"
            )

        self._username = username
        self.profile = profile

    @property
    def username(self) -> str:
        return self._username

    def info(self) -> str:
        return f"User {self.username} | {self.profile.short()}"


def main() -> None:
    try:
        profile = Profile(age=24, bio="My full name is Danil Korovin.")
        user = User(username="RizzZzz", profile=profile)
    except (InvalidAge, InvalidUsername) as error:
        print(f"> {error}")
    else:
        print(user.info())


if __name__ == "__main__":
    main()
