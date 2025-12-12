import time
from functools import wraps
from typing import Callable, ParamSpec, TypeVar, Union

R = TypeVar("R")
P = ParamSpec("P")


def timeit(func: Callable[P, R]) -> Callable[P, R]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        lead_time = round((end_time - start_time), 3)

        print(f"Итоговое время работы функции {func.__name__}: {lead_time} seconds")
        return result

    return wrapper


@timeit
def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    time.sleep(2)
    return a + b


def main() -> None:
    result = add(1, 2)
    print(f"Результат: {result}")

    print(f"\nНазвание функции: {add.__name__}")
    print(getattr(add, "__annotations__", {}))


if __name__ == "__main__":
    main()
