def main():
    data = [[1, 2], [3, 4]]
    keys = tuple(tuple(lst) for lst in data)

    print(keys)


if __name__ == "__main__":
    main()
