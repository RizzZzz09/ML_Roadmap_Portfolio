from dataclasses import dataclass, field


@dataclass
class Book:
    title: str
    author: str
    year: int
    tags: list[str] = field(default_factory=list)
    rating: float = 0.0


def main() -> None:
    book = Book("test_title", "random_author", 2025)
    print(book)

    book.tags.append("random_tag")
    book.tags.append("my_random_tag")

    print(book)


if __name__ == "__main__":
    main()
