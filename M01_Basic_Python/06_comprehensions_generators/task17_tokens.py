def main(text):
    words_only = text.split()
    for word in words_only:
        yield word


if __name__ == "__main__":
    gen = main("Machine learning is fun and powerful")
    for _ in range(5):
        print(next(gen))
