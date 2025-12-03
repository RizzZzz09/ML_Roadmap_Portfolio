from datetime import datetime


class Logger:
    def log(self, message: str) -> str:
        return message


class TimestampLogger(Logger):
    def log(self, message: str) -> str:
        now = datetime.now().strftime("%H:%M:%S")
        log = super().log(message)
        return f"[{now}] {log}"


def main() -> None:
    message = "Hello, how are you?"
    timestamp_logger = TimestampLogger()
    print(timestamp_logger.log(message))


if __name__ == "__main__":
    main()
