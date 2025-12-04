from dataclasses import dataclass


@dataclass
class LogRecord:
    level: int
    message: str
    source: str


def main() -> None:
    first_log = LogRecord(1, "Hello!", "RizzZzz@gmail.com")
    second_log = LogRecord(1, "Hello!", "RizzZzz@gmail.com")

    print(first_log)
    print(second_log)

    print(first_log == second_log)


if __name__ == "__main__":
    main()
