def main():
    text = "Hello, hello world!"
    result = set(text.lower().replace(",", " ").replace("!", " ").split())
    print(len(result))


if __name__ == "__main__":
    main()
