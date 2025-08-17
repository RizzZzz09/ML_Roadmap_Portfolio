def multiply(a: int, b: int) -> int:
    return a * b


if __name__ == "__main__":
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    result = multiply(first_number, second_number)
    print(f"Result: {result}")
