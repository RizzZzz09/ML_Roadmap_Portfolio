from itertools import chain, zip_longest


def main():
    ids = [1, 2, 3]
    names = ["Alice", "Bob"]

    print(list(chain(ids, names)))
    print(list(zip_longest(ids, names, fillvalue="-")))


if __name__ == "__main__":
    main()
