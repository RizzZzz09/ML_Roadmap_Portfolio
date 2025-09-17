from itertools import chain, zip_longest


def main():
    list1 = [1, 2, 3]
    list2 = ["a", "b"]

    print(list(chain(list1, list2)))
    print(list(zip_longest(list1, list2, fillvalue="-")))


if __name__ == "__main__":
    main()
