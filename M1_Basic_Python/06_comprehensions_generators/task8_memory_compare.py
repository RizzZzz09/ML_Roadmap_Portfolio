import sys


def main():
    list_comprehension = [number**2 for number in range(1, 1_000_001)]
    generator_expression = (number**2 for number in range(1, 1_000_001))

    print(sys.getsizeof(list_comprehension))
    print(sys.getsizeof(generator_expression))


if __name__ == "__main__":
    main()
