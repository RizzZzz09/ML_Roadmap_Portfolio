def main():
    n = int(input("Enter any number: "))
    for num in range(1, n + 1):
        if num % 2 == 0:
            continue
        print(num)


if __name__ == "__main__":
    main()
