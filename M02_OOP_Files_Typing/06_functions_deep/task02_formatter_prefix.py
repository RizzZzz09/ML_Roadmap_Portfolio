from typing import Callable


def formatter(prefix: str) -> Callable[[str], str]:
    def log(message: str) -> str:
        return f"{prefix}: {message}"

    return log


def main() -> None:
    error_text = formatter("ERROR")
    text = error_text("Everything is wrong")
    print(text)


if __name__ == "__main__":
    main()
