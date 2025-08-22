def main():
    result = 1
    n = int(input("Enter any number: "))
    for number in range(1, n + 1):
        result *= number
    print(result)


if __name__ == "__main__":
    main()
