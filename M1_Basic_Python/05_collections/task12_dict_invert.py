def main():
    data = {"a": 1, "b": 1, "c": 2}
    counter = {}

    for key, value in data.items():
        counter.setdefault(value, []).append(key)

    for k in counter:
        counter[k].sort()

    print(counter)


if __name__ == "__main__":
    main()
