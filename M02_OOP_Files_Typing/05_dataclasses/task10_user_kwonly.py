from dataclasses import dataclass


@dataclass(kw_only=True)
class User:
    username: str
    age: int


def main() -> None:
    """
    try:
        user = User("Danil", 24)
    except TypeError as error:
        print(f"> Ошибка: {error}.\n> Создаётся новый объект:")
        user = User(username="Danil", age=24)
    finally:
        print(user)
    """


if __name__ == "__main__":
    main()
