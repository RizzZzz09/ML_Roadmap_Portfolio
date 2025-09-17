from itertools import islice


def batched(iterable, n):
    it = iter(iterable)
    while True:
        batche = list(islice(it, n))
        if not batche:
            break
        yield batche


def main():
    for batche in batched(range(1, 21), 3):
        print(batche)


if __name__ == "__main__":
    main()
