from functools import wraps
from typing import Callable, ParamSpec, TypeVar

R = TypeVar("R")
P = ParamSpec("P")


def method_logger(func: Callable[P, R]) -> Callable[P, R]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"Вызов метода {func.__name__} c args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper


class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @method_logger
    def greet(self) -> str:
        return f"{self.name} is {self.age} years old"


def main() -> None:
    user = User("Danil", 24)
    user.greet()


if __name__ == "__main__":
    main()
