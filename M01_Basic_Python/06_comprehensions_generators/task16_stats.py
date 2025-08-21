def main():
    data = [10, 20, 30, 40, 50]

    names = ["minimum", "maximum", "mean", "std"]
    values = [
        min(data),
        max(data),
        sum(data) / len(data),
        ((sum((x - sum(data) / len(data)) ** 2 for x in data) / len(data)) ** 0.5),
    ]

    result = {key: value for key, value in zip(names, values, strict=False)}
    print(result)


if __name__ == "__main__":
    main()
