def main():
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    operation = input('Enter the operation "+", "-", "*" or "/": ').strip()

    match operation:
        case "+":
            print(f"Result: {first_number + second_number}")
        case "-":
            print(f"Result: {first_number - second_number}")
        case "*":
            print(f"Result: {first_number * second_number}")
        case "/":
            if second_number == 0:
                print("Division by zero is not allowed")
            else:
                print(f"Result: {first_number / second_number}")
        case _:
            print("Unknown operation")


if __name__ == "__main__":
    main()
