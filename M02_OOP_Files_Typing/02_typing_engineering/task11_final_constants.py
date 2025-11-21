from typing import Final

MAX_USERS: Final = 300
API_VERSION: Final = "v1"
PI: Final = 3.14159


def describe_limits() -> str:
    return f"Config: MAX_USERS={MAX_USERS}, API_VERSION={API_VERSION}, PI={PI}"


def main() -> None:
    result = describe_limits()
    print(result)


if __name__ == "__main__":
    main()
