import random


def main():
    random_numbers = [random.random() for _ in range(3)]  # noqa: F841
    state = random.getstate()
    after = [random.random() for _ in range(3)]
    random.setstate(state)
    continue_numbers = [random.random() for _ in range(3)]

    print(f"First sequence after state restore is equal: {after == continue_numbers}")


if __name__ == "__main__":
    main()
