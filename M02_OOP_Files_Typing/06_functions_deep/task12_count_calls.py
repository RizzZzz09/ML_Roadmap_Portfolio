from functools import wraps
from typing import Callable, ParamSpec, TypeVar

R = TypeVar("R")
P = ParamSpec("P")


def count_calls(func: Callable[P, R]) -> Callable[P, R]:
    attr_name = f"_calls_{func.__name__}"

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        self = args[0]

        if not hasattr(self, attr_name):
            setattr(self, attr_name, 0)

        current = getattr(self, attr_name) + 1
        setattr(self, attr_name, current)

        print(f"Метод {func.__name__} вызван {current} раз")

        return func(*args, **kwargs)

    return wrapper


class Counter:
    @count_calls
    def increment(self) -> None:
        print("increment called")


def main() -> None:
    a = Counter()
    b = Counter()

    a.increment()
    a.increment()
    b.increment()
    a.increment()


if __name__ == "__main__":
    main()
