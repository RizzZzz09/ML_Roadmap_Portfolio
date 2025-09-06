import random


def main():
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(f"Original: {number_list}")
    random.shuffle(number_list)
    print(f"Mixed: {number_list}")


if __name__ == "__main__":
    main()
