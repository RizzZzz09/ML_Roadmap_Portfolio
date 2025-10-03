def main():
    while True:
        try:
            number_input = input("Enter number: ")
            if number_input.lower() == "q":
                break
            number = int(number_input)
        except ValueError:
            print("You did not enter a number")
        else:
            print(f"The input is correct: {number}")


if __name__ == "__main__":
    main()
