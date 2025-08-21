def main():
    pairs = [(1, 2), (2, 1), (3, 4), (4, 3), (5, 6)]
    unique_couples = {tuple(sorted(pair)) for pair in pairs}

    print(unique_couples)


if __name__ == "__main__":
    main()
