from itertools import islice
from typing import Iterator


def clipped_backoff(base: float, max_delay: float) -> Iterator[float]:
    delay = float(base)
    while True:
        yield delay if delay <= max_delay else float(max_delay)
        delay *= 2.0


def backoff_schedule(base: float, retries: int, max_delay: float) -> Iterator[tuple[float, float]]:
    total = 0.0
    for d in islice(clipped_backoff(base, max_delay), max(0, retries)):
        total += d
        yield d, total


def prompt_float(label: str, positive: bool = False) -> float:
    while True:
        raw = input(f"{label}: ").strip()
        try:
            val = float(raw)
            if positive and val <= 0:
                print("Value must be > 0. Try again.")
                continue
            return val
        except ValueError:
            print("Enter a number, e.g. 1 or 2.5")


def prompt_int(label: str, non_negative: bool = False) -> int:
    while True:
        raw = input(f"{label}: ").strip()
        try:
            val = int(raw)
            if non_negative and val < 0:
                print("Value must be >= 0. Try again.")
                continue
            return val
        except ValueError:
            print("Enter an integer, e.g. 0, 3, 10")


def main() -> None:
    print("Backoff schedule (interactive mode)")
    base = prompt_float("Enter base (seconds, > 0)", positive=True)
    retries = prompt_int("Enter retries (attempts count, >= 0)", non_negative=True)
    max_delay = prompt_float("Enter max_delay (seconds)", positive=False)

    if base <= 0:
        print("Invalid input: base must be > 0")
        return

    for delay, at in backoff_schedule(base, retries, max_delay):
        print(f"delay={delay} at={at}")


if __name__ == "__main__":
    main()
