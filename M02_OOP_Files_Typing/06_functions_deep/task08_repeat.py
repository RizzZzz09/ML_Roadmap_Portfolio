from datetime import datetime
from functools import wraps
from typing import Callable, ParamSpec, TypeVar

R = TypeVar("R")
P = ParamSpec("P")


class InvalidNumberOfRepetitions(Exception):
    """Ошибка. Выбрасывается, если кол-во повторений неположительное число."""

    pass


def repeat(number_of_repetitions: int) -> Callable[[Callable[P, R]], Callable[P, R]]:
    if number_of_repetitions <= 0:
        raise InvalidNumberOfRepetitions(
            f"Кол-во повторений number_of_repetitions={number_of_repetitions} "
            f"не может быть неположительным числом"
        )

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            # Для избежания ошибки: Local variable 'result' might be referenced before assignment
            result: R | None = None

            for _ in range(number_of_repetitions):
                result = func(*args, **kwargs)

            assert result is not None
            return result

        return wrapper

    return decorator


@repeat(number_of_repetitions=3)
def greet(name: str) -> str:
    print(f"Hello {name}")
    return name.upper()


@repeat(number_of_repetitions=3)
def time_now() -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"The time is now: {now}")
    return now


def main() -> None:
    result = greet("Danil")
    print(result)

    time = time_now()
    print(time)

    print(f"\nНазвание функции: {greet.__name__}")
    print(getattr(greet, "__annotations__", {}))

    print(f"\nНазвание функции: {time_now.__name__}")
    print(getattr(time_now, "__annotations__", {}))


if __name__ == "__main__":
    main()
