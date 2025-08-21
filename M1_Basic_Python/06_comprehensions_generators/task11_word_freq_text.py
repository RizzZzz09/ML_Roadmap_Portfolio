def main():
    text = "Machine learning is fun and machine learning is powerful"
    words_list = text.lower().split()
    counter_words = {key: sum(1 for word in words_list if word == key) for key in set(words_list)}
    top_three_words = sorted(counter_words.items(), key=lambda item: (-item[1], item[0]))[:3]
    print(top_three_words)


if __name__ == "__main__":
    main()
