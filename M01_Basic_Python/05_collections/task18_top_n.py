def main():
    freqs = {"cat": 3, "dog": 5, "bird": 2}
    n = 2

    sorted_freqs = sorted(freqs.items(), key=lambda x: (-x[1], x[0]))
    top_words = sorted_freqs[:n]
    print(top_words)


if __name__ == "__main__":
    main()
