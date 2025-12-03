class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

    def info(self) -> str:
        return f"User {self.username} ({self.email})"

    @classmethod
    def from_string(cls, raw: str) -> "User":
        data = raw.split("|")
        return cls(data[0], data[1])


def main() -> None:
    raw = "RizzZzz|abc@gmail.com"
    user = User.from_string(raw)
    print(user.info())


if __name__ == "__main__":
    main()
