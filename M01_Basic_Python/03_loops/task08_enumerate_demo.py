def main():
    word = input("Enter a word: ")
    for index, char in enumerate(word):
        print(f"{index} -> {char}")


if __name__ == "__main__":
    main()
