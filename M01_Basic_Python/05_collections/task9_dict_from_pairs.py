def main():
    pairs = [("a", 1), ("b", 2), ("a", 3), ("c", 5), ("b", 4)]
    counter = {}

    for key, value in pairs:
        counter[key] = counter.get(key, 0) + value

    print(counter)


if __name__ == "__main__":
    main()
