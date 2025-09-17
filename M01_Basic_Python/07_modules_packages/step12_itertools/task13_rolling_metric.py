from collections import deque
from itertools import islice


def rolling(numbers: list[int]):
    max_len_window = 5
    dp = deque(islice(numbers, max_len_window), maxlen=max_len_window)
    yield list(dp)
    for number in numbers[max_len_window:]:
        dp.append(number)
        yield list(dp)


def avg(window: list[int]) -> float:
    return sum(window) / len(window)


def main():
    numbers = [number for number in range(1, 21)]
    for window in rolling(numbers):
        arithmetic_mean = avg(window)
        print(f"{window}, avg = {arithmetic_mean}")


if __name__ == "__main__":
    main()
