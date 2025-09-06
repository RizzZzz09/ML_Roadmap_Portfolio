import random


def main():
    fruits = ["apple", "banana", "cherry"]

    print(f"One fruit: {random.choice(fruits)}")
    print(f"With repetition: {random.choices(fruits, k=5)}")
    print(f"Without repetition: {random.sample(fruits, k=2)}")


if __name__ == "__main__":
    main()
