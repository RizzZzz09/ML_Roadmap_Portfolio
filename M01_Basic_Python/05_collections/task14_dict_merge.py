def main():
    user1 = {"name": "Alice", "age": 25}
    user2 = {"age": 30, "city": "Riga"}

    user1.update(user2)

    # merged = user1 | user2

    print(user1)


if __name__ == "__main__":
    main()
