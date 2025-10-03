import random
import time


def unstable():
    if random.random() < 0.5:
        raise RuntimeError("Glitch!")
    return "Success"


def retry(fn, attempts=3, base_delay=0.5):
    for attempt in range(attempts):
        try:
            return fn()
        except RuntimeError as error:
            print(f"attempt: {attempt + 1} failed: {error}")
            if attempt == attempts - 1:
                raise
            delay = base_delay * (2**attempt)
            print(f"We're waiting {delay} seconds")
            time.sleep(delay)


if __name__ == "__main__":
    result = retry(unstable)
    print("Result:", result)
