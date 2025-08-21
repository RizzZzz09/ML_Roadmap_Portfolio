def main():
    words = ["cat", "dog", "cat", "bird", "dog", "cat"]
    count = {}

    for word in words:
        count[word] = count.get(word, 0) + 1

    print(count)


if __name__ == "__main__":
    main()
