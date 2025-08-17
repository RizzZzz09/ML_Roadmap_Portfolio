def get_person():
    user_name = input("What is your name: ")
    user_age = int(input("How old are you: "))
    return user_name, user_age


if __name__ == "__main__":
    name, age = get_person()
    print(f"Name: {name}, age: {age}")
