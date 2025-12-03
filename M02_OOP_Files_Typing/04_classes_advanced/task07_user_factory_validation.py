from typing import Union


class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

    def info(self) -> str:
        return f"User {self.username} ({self.email})"

    @classmethod
    def from_string(cls, raw: str) -> Union["User", None]:
        data = raw.split("|")
        correct_email = cls.validate_email(data[1])
        if correct_email:
            return cls(data[0], data[1])
        return None

    @staticmethod
    def validate_email(email: str) -> bool:
        if not email or "@" not in email:
            return False
        return True


def main() -> None:
    raw = "RizzZzz|abc@gmail.com"
    user = User.from_string(raw)
    if user is None:
        print("Invalid data!")
    else:
        print(user.info())


if __name__ == "__main__":
    main()
