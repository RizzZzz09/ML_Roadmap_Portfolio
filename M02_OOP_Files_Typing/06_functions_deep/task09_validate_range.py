from functools import wraps
from typing import Callable, ParamSpec, TypeVar

MIN_VALUE = 0
MAX_VALUE = 100

R = TypeVar("R")
P = ParamSpec("P")


class InvalidValue(Exception):
    """Ошибка. Выбрасывается, если аргумент функции не удовлетворяет условию min <= n <= max."""

    pass


def validate_range(min_value: int, max_value: int) -> Callable[[Callable[P, R]], Callable[P, R]]:
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            if args and isinstance(args[0], (int, float)) and not min_value <= args[0] <= max_value:
                raise InvalidValue(
                    f"Значение [{args[0]}] "
                    f"не удовлетворяет условию {min_value} <= n <= {max_value}"
                )
            return func(*args, **kwargs)

        return wrapper

    return decorator


@validate_range(MIN_VALUE, MAX_VALUE)
def square(x: int) -> int:
    return x**2


def main() -> None:
    for number in range(-50, 151):
        try:
            print(square(number))
        except InvalidValue as error:
            print(f"> {error}")

    print(f"\nНазвание функции: {square.__name__}")
    print(getattr(square, "__annotations__", {}))


if __name__ == "__main__":
    main()
