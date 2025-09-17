from itertools import filterfalse


def main():
    even = list(filterfalse(lambda x: x % 2, range(1, 31)))
    result = list(filter(lambda x: x % 3 == 0, even))
    print(list(result))


if __name__ == "__main__":
    main()
