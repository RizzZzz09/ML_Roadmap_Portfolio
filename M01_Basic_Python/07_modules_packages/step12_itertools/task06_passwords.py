from itertools import islice, product


def main():
    for pwd in islice(product("abc123", repeat=4), 10):
        print("".join(pwd))


if __name__ == "__main__":
    main()
