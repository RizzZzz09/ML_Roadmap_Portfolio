from datetime import datetime
from typing import Protocol


class Writer(Protocol):
    def write(self, message: str) -> None: ...


class Sender(Protocol):
    def connect(self) -> None: ...

    def send(self, message: str) -> None: ...

    def close(self) -> None: ...


class ConsoleWriter:
    def write(self, message: str) -> None:
        print(f"[LOG] {message}")


class NetworkSender:
    def connect(self) -> None:
        print(f"[{datetime.now().strftime('%H:%M:%S %d.%m.%Y')}] Подключение к сети.")

    def send(self, message: str) -> None:
        print(
            f"[{datetime.now().strftime('%H:%M:%S %d.%m.%Y')}] Сообщение \"{message}\" отправлено."
        )

    def close(self) -> None:
        print(f"[{datetime.now().strftime('%H:%M:%S %d.%m.%Y')}] Программа завершена.")


def log_message(conn: Writer, message: str) -> None:
    conn.write(message)


def process_connection(conn: Sender, message: str) -> None:
    conn.connect()
    conn.send(message)
    conn.close()


def main() -> None:
    writer = ConsoleWriter()
    sender = NetworkSender()
    message = "How are you doing?"

    log_message(writer, message)
    process_connection(sender, message)


if __name__ == "__main__":
    main()
