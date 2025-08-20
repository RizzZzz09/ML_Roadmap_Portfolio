def main():
    data = [("Alice", 80), ("Bob", 95), ("Carol", 70)]

    maximum = max(data, key=lambda x: x[-1])
    scores = sorted([score for _, score in data])

    mid = len(scores) // 2

    if len(scores) % 2 != 0:
        median = scores[mid]
    else:
        median = (scores[mid - 1] + scores[mid]) / 2

    print(median)
    print(maximum)


if __name__ == "__main__":
    main()
