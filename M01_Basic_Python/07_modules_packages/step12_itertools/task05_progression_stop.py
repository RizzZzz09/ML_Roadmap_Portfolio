from itertools import count


def main():
    for number in count(1, 3):
        if number > 50:
            break
        print(number)


if __name__ == "__main__":
    main()
