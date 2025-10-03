def main():
    try:
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))

        print(f"Result: {first_number / second_number}")
    except (ValueError, ZeroDivisionError) as error:
        print(f"Error: {error}")
    else:
        print("Successfully")


if __name__ == "__main__":
    main()
