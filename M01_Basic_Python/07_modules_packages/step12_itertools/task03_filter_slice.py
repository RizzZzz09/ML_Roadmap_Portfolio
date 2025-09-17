from itertools import filterfalse, islice


def main():
    number_list = [number for number in range(21)]
    print(list(filterfalse(lambda x: x % 2, islice(number_list, 5, 16))))


if __name__ == "__main__":
    main()
