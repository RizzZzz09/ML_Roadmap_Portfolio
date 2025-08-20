def main():
    text = "Hello, World!"
    counter = {}

    for char in text.lower():
        if char.isalpha():
            counter[char] = counter.get(char, 0) + 1

    print(counter)


if __name__ == "__main__":
    main()
