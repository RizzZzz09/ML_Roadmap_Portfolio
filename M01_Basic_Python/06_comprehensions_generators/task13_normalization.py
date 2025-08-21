def main():
    data = [10, 20, 30, 40, 50]
    minimum = min(data)
    maximum = max(data)

    normal_appearance = [(number - minimum) / (maximum - minimum) for number in data]
    print(normal_appearance)


if __name__ == "__main__":
    main()
