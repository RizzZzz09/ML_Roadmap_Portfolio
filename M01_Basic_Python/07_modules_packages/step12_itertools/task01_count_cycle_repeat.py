from itertools import count, cycle, islice, repeat


def main():
    for number in islice(count(100, 10), 5):
        print(number)

    colors = cycle(["red", "green", "blue"])
    for color in islice(colors, 6):
        print(color)

    for text in repeat("Hi", 4):
        print(text)


if __name__ == "__main__":
    main()
