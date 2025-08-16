def main():
    number = int(input("Enter any number: "))

    if number <= 1:
        print("Not prime")
        return

    divider = 2
    while divider * divider <= number:
        if number % divider == 0:
            print("Not prime")
            break
        divider += 1
    else:
        print("Prime")


if __name__ == "__main__":
    main()
