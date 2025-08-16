def main():
    side = int(input("Enter any number: "))
    for _ in range(1, side + 1):
        result = ""
        for _ in range(1, side + 1):
            result += "*"
        print(result)


if __name__ == "__main__":
    main()
