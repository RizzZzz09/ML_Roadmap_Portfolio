def print_hello(name: str) -> None:
    print(f"Hello, {name}!")


def main() -> None:
    name = input("What is your name: ")
    print_hello(name)


if __name__ == "__main__":
    main()
