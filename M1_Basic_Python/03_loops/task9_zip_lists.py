def main():
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]

    for name, age in zip(names, ages, strict=False):
        print(f"{name} - {age}")


if __name__ == "__main__":
    main()
