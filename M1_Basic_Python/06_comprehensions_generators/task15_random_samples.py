import random


def main(data):
    while True:
        yield random.choice(data)


if __name__ == "__main__":
    gen = main(data=[1, 2, 3, 4, 5])
    for _ in range(5):
        print(next(gen))
