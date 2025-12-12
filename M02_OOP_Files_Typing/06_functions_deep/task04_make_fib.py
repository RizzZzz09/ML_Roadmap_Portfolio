from typing import Callable


def make_fib() -> Callable[[int], int]:
    cache = [0, 1]

    def fib(index: int) -> int:
        if index < len(cache):
            return cache[index]
        else:
            fib1, fib2 = cache[-2], cache[-1]
            while len(cache) <= index:
                fib1, fib2 = fib2, fib1 + fib2
                cache.append(fib2)
            return cache[index]

    return fib


def main() -> None:
    fib = make_fib()
    print(fib(11))


if __name__ == "__main__":
    main()
