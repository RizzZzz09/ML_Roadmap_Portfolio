from typing import Protocol


class Sender(Protocol):
    def send(self, recipient: str, message: str) -> str: ...


class EmailSender:
    def send(self, recipient: str, message: str) -> str:
        return f"EMAIL to {recipient}: {message}"


class SmsSender:
    def send(self, recipient: str, message: str) -> str:
        return f"SMS to {recipient}: {message}"


class NotificationService:
    def __init__(self, sender: Sender):
        self.sender = sender

    def notify(self, recipient: str, message: str) -> str:
        return self.sender.send(recipient, message)


def main() -> None:
    email_sender = EmailSender()
    sms_sender = SmsSender()

    email_service = NotificationService(email_sender)
    sms_service = NotificationService(sms_sender)

    print(email_service.notify("RizzZzz@gmail.com", "Hello!"))
    print(sms_service.notify("RizzZzz@gmail.com", "Hello!"))


if __name__ == "__main__":
    main()
