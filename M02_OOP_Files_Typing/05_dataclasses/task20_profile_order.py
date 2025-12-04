from dataclasses import dataclass, field


@dataclass
class UserProfile:
    username: str
    email: str
    active: bool = True
    roles: list[str] = field(default_factory=list)
    normalized_email: str = field(init=False)

    def __post_init__(self) -> None:
        self.normalized_email = self.email.strip().lower()


def main() -> None:
    user_profile = UserProfile("RizzZzz", "   RizzzZZZZZ@gmail.com")
    user_profile.roles.append("base_user")
    print(user_profile)


if __name__ == "__main__":
    main()
