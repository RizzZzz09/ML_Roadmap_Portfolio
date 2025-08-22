def main():
    user_age = int(input("How old are you: "))

    if user_age < 18:
        print("Minor")
    else:
        print("Adult")


if __name__ == "__main__":
    main()
