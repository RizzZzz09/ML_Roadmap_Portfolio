from typing import Callable, ParamSpec, TypeVar

T = TypeVar("T", int, float)
R = TypeVar("R")
P = ParamSpec("P")


def log_calls(func: Callable[P, R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"Вызов функции {func.__name__} с аргументами args={args}, kwargs={kwargs}.")
        return func(*args, **kwargs)

    return wrapper


@log_calls
def add(a: T, b: T) -> T:
    return a + b


def main() -> None:
    a = 10
    b = 3

    result = add(a, b)
    print(result)


if __name__ == "__main__":
    main()
