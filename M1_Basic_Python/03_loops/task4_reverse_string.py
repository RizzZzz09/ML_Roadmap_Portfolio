def main():
    word = input("Enter a word: ")
    result = ""
    for char in word:
        result = char + result
    print(result)


if __name__ == "__main__":
    main()
