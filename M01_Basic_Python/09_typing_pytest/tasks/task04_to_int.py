def to_int(number: str) -> int | None:
    try:
        return int(number)
    except ValueError:
        return None


def main() -> None:
    entrance = ["4", "number"]
    for value in entrance:
        print(to_int(value))


if __name__ == "__main__":
    main()
