from datetime import datetime
from functools import wraps
from typing import Callable, ParamSpec, TypeVar, Union

R = TypeVar("R")
P = ParamSpec("P")


def simple_logger(func: Callable[P, R]) -> Callable[P, R]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start_time = datetime.now().strftime("%H:%M:%S")
        print(f"Начало работы функции {func.__name__}: {start_time}")

        print(f"- Аргументы функции: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"- Результат: {result}")

        end_time = datetime.now().strftime("%H:%M:%S")
        print(f"Окончание работы функции {func.__name__}: {end_time}")
        return result

    return wrapper


@simple_logger
def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x + y


def main() -> None:
    a, b = 10, 12
    add(a, b)

    print(f"\nНазвание функции: {add.__name__}")
    print(getattr(add, "__annotations__", {}))


if __name__ == "__main__":
    main()
