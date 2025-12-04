from dataclasses import dataclass


@dataclass
class User:
    user_name: str
    email: str


@dataclass
class Admin(User):
    is_superuser: bool = True


def main() -> None:
    user = User("RizzZzz", "rizzzzzz@gmail.com")
    admin = Admin("admin", "admin@gmail.com")

    print(user)
    print(admin)


if __name__ == "__main__":
    main()
