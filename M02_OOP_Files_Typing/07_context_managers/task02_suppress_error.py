import time
from types import TracebackType
from typing import Self


class SuppressError:
    def __init__(self, error: type[BaseException]) -> None:
        self.error = error

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> bool | None:
        if self.error == exc_type:
            return True
        return None


def main() -> None:
    with SuppressError(ValueError):
        int("abc")  # ValueError → __exit__ вернул True → ошибки нет

    time.sleep(1)


"""
    with SuppressError(ValueError):
        1 / 0  # ZeroDivisionError → __exit__ вернул None → ошибка летит
"""

if __name__ == "__main__":
    main()
