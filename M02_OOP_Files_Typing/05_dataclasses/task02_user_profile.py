from dataclasses import dataclass


@dataclass
class UserProfile:
    username: str
    email: str
    age: int


def main() -> None:
    first_user = UserProfile("RizzZzz", "rizzzzz@gmail.com", 21)
    second_user = UserProfile("Faust09_009", "abc1223@gmail.com", 24)
    third_user = UserProfile("RizzZzz", "rizzzzz@gmail.com", 21)

    print(first_user)
    print(second_user)
    print(third_user)

    print(first_user == second_user)
    print(first_user == third_user)


if __name__ == "__main__":
    main()
