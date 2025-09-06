import random
import string


def main():
    numbers = string.digits
    letters = string.ascii_letters

    random_password = "".join(random.choices(numbers + letters, k=16))
    print(random_password)


if __name__ == "__main__":
    main()
