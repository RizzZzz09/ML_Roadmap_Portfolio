from dataclasses import dataclass, field


@dataclass
class User:
    """
    tags: list[str] = []
    """

    tags: list[str] = field(default_factory=list)


def main() -> None:
    first_user = User()
    second_user = User()

    first_user.tags.append("ml")
    print(second_user)


if __name__ == "__main__":
    main()
