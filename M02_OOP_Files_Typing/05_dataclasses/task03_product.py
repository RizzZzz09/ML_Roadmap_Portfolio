from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float


def main() -> None:
    book = Product("Alice's Adventures in Wonderland", 10)
    game = Product("Fallout 4", 70)

    print(book)
    print(game)

    print(book == game)

    print(book.name)
    print(book.price)


if __name__ == "__main__":
    main()
