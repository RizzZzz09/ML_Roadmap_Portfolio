import random


def main():
    random_throws = [random.randint(1, 6) for _ in range(20)]
    print(f"Throws: {random_throws}")

    grouping = {}
    for number in random_throws:
        grouping[number] = grouping.get(number, 0) + 1

    print(f"Statistics: {grouping}")


if __name__ == "__main__":
    main()
