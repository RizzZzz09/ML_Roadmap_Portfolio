import time


def main():
    user_input = int(input("Where to start the countdown: "))
    if user_input < 0:
        print("The number cannot be less than or equal to zero.")
        return

    while user_input >= 0:
        print(f"Left: {user_input} sec")
        time.sleep(1)
        user_input -= 1

    print("The countdown is over")


if __name__ == "__main__":
    main()
