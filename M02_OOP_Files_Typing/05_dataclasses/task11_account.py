from dataclasses import dataclass, field


@dataclass
class Account:
    login: str
    password: str = field(repr=False)


def main() -> None:
    my_account = Account("RizzZzz09_009", "myPassword")
    print(my_account)
    print(my_account.password)


if __name__ == "__main__":
    main()
