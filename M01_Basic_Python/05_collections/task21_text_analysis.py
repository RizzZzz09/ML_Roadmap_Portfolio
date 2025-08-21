def main():
    text = "Hello, hello world! This is a simple world. Hello again!"
    clear_text = "".join(char if char.isalnum() or char.isspace() else "" for char in text).lower()
    words_only_list = clear_text.split()

    top_words = {}
    for word in words_only_list:
        top_words[word] = top_words.get(word, 0) + 1

    the_most_common_word = max(top_words.items(), key=lambda item: item[1])

    print(f"The most common word: {the_most_common_word[0]}")
    print(f"Number of unique words: {len(set(top_words))}")

    sorted_top_word = sorted(top_words.items(), key=lambda item: (-item[1], item[0]))
    print(f"Top 3 words: {sorted_top_word[:3]}")


if __name__ == "__main__":
    main()
