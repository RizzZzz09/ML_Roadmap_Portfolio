def main():
    data = [("fruit", "apple"), ("veg", "carrot"), ("fruit", "banana")]
    grouping = {}

    for category, value in data:
        grouping.setdefault(category, []).append(value)

    print(grouping)


if __name__ == "__main__":
    main()
