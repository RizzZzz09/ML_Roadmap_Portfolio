def length_safe(s: str | None) -> int:
    if s is not None:
        return len(s)
    return 0


def main() -> None:
    string = "12345"
    print(length_safe(string))


if __name__ == "__main__":
    main()
