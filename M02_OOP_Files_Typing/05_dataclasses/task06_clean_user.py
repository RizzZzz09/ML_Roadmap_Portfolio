from dataclasses import dataclass


@dataclass
class CleanUser:
    username: str
    email: str

    def __post_init__(self) -> None:
        self.username = self.username.strip()
        self.email = self.email.strip().lower()


def main() -> None:
    user = CleanUser("  RizzZzz    ", "RIZZZZZ@GMAIL.com             ")
    print(user)
    print(user.username)
    print(user.email)


if __name__ == "__main__":
    main()
