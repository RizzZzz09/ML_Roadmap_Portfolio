import random


def main():
    result_list = [random.uniform(-1, 1) for _ in range(10)]
    print(result_list)


if __name__ == "__main__":
    main()
