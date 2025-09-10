from collections import Counter


def main():
    text = """Python is a powerful programming language.
It is widely used in data science, web development, and automation.
Many developers love Python because it is simple and readable.

Java is also a popular programming language.
It is often used in enterprise systems, mobile applications, and backend development.
Unlike Python, Java is more strict with syntax."""

    text_list = text.split("\n\n")
    first_text = "".join(char.lower() for char in text_list[0] if char.isalnum() or char.isspace())
    second_text = "".join(
        char.lower() for char in text_list[-1] if char.isalnum() or char.isspace()
    )

    counter_first_text = Counter(first_text.replace("\n", " ").split())
    counter_second_text = Counter(second_text.replace("\n", " ").split())

    print("[UNION]")
    union = (counter_first_text | counter_second_text).most_common(10)
    for word in union:
        print(f"{word[0]}: {word[-1]}")

    print("\n[INTERSECTION]")
    intersection = counter_first_text & counter_second_text
    for word in intersection.items():
        print(f"{word[0]}: {word[-1]}")

    print("\n[UNIQUE TO FIRST]")
    unique_to_first = (counter_first_text - counter_second_text).most_common(10)
    for word in unique_to_first:
        print(f"{word[0]}: {word[-1]}")


if __name__ == "__main__":
    main()
