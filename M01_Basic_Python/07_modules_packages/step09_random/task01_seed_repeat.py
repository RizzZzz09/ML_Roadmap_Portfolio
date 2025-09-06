import random


def main():
    random.seed(123)
    result_list = [random.random() for _ in range(5)]
    print(result_list)


if __name__ == "__main__":
    main()
