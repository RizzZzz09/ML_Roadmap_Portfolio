import time
from functools import lru_cache


@lru_cache(maxsize=None)
def slow_square(number: int) -> int:
    time.sleep(1)
    return number**2


def main() -> None:
    print(slow_square(10))
    print(slow_square(10))
    print(slow_square(20))
    print(slow_square(10))

    print(slow_square.cache_info())


if __name__ == "__main__":
    main()
