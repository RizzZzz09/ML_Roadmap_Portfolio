import time
from types import TracebackType
from typing import Self


class Timer:
    def __init__(self) -> None:
        self.start: float | None = None
        self.end: float | None = None

    def __enter__(self) -> Self:
        self.start = time.perf_counter()
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        self.end = time.perf_counter()
        if self.start is not None:
            print(self.end - self.start)


def main() -> None:
    i = 0
    with Timer():
        for _ in range(1_000_000):
            i += 1


if __name__ == "__main__":
    main()
