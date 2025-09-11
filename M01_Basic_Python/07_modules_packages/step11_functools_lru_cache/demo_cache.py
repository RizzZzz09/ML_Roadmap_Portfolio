import math
import time
from functools import lru_cache

COMMAND = {
    "--start-test": "Start 1000 iteration",
    "--maxsize": "Set cache size",
    "--typed": "Set strong typing of keys",
    "--clear-cache": "Cleaning cache",
}
NUMBER_FOR_TEST = 5


def _core(x: int) -> int:
    total = 0
    for i in range(100_000):
        total += int(math.sqrt((x * i + 1) ** 3) % 1234567)
    return total % 1_000_000


def slow_transform(x: int) -> int:
    return _core(x)


def build_cached(_maxsize=None, _typed=False):
    @lru_cache(maxsize=_maxsize, typed=_typed)
    def cached(x: int) -> int:
        return _core(x)

    return cached


def show_commands(commands: dict[str, str]):
    print("All commands:".upper())
    i = 1
    for command, description in commands.items():
        print(f"\t{i}. {command} - {description}")
        i += 1


def start_test(func_for_test, *args):
    start_time = time.perf_counter()
    for _ in range(1_000):
        func_for_test(*args)
    end_time = time.perf_counter()
    duration = end_time - start_time
    print(f"Function execution time: {duration} seconds.")

    if hasattr(func_for_test, "cache_info"):
        info = func_for_test.cache_info()
        for name, value in zip(("hits", "misses", "maxsize", "currsize"), info, strict=False):
            print(name, value)


if __name__ == "__main__":
    show_commands(COMMAND)
    maxsize = None
    typed = False
    cached_func = build_cached(_maxsize=maxsize, _typed=typed)

    while True:
        user_input = input("> ").lower().split()

        match user_input[0]:
            case "--start-test":
                start_test(slow_transform, NUMBER_FOR_TEST)
                start_test(cached_func, NUMBER_FOR_TEST)

            case "--maxsize":
                maxsize = int(user_input[-1])
                cached_func = build_cached(_maxsize=maxsize, _typed=typed)

            case "--typed":
                if user_input[-1].lower() == "true":
                    typed = True
                elif user_input[-1].lower() == "false":
                    typed = False
                else:
                    print("You must enter True/False")
                    continue

                cached_func = build_cached(_maxsize=maxsize, _typed=typed)

            case "--clear-cache":
                cached_func.cache_clear()
                print("Cache cleared!")
                info = cached_func.cache_info()
                for name, value in zip(
                    ("hits", "misses", "maxsize", "currsize"), info, strict=False
                ):
                    print(name, value)

            case _:
                print("Unknown command")
                continue
