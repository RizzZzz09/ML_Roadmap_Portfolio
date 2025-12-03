class Sender:
    sender_type = "base"

    def send(self, recipient: str, message: str) -> str:
        return ""


class EmailSender(Sender):
    sender_type = "email"

    def send(self, recipient: str, message: str) -> str:
        return f"EMAIL to {recipient}: {message}"


class SmsSender(Sender):
    sender_type = "sms"

    def send(self, recipient: str, message: str) -> str:
        return f"SMS to {recipient}: {message}"


class MessageBuilder:
    @staticmethod
    def clean(text: str) -> str:
        return text.replace("  ", " ").strip()

    @classmethod
    def from_sender(cls, sender_name: str) -> str:
        match sender_name:
            case "email":
                return "EMAIL MESSAGE"
            case "sms":
                return "SMS MESSAGE"
            case _:
                return "UNKNOWN"


class NotificationService:
    def __init__(self, sender: Sender, builder: MessageBuilder):
        self.sender = sender
        self.builder = builder

    def notify(self, recipient: str, message: str) -> str:
        clean_message = self.builder.clean(message)
        prefix = self.builder.from_sender(self.sender.sender_type)
        final_message = prefix + " " + clean_message

        return self.sender.send(recipient, final_message)


def main() -> None:
    email_sender = EmailSender()
    sms_sender = SmsSender()
    builder = MessageBuilder()

    email_service = NotificationService(email_sender, builder)
    sms_service = NotificationService(sms_sender, builder)

    print(email_service.notify("RizzZzz@gmail.com", "        Hello! "))
    print(sms_service.notify("RizzZzz@gmail.com", "        Hello,  RizzZzz! "))


if __name__ == "__main__":
    main()
