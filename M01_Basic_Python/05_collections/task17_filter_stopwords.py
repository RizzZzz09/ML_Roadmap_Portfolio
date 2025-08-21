def main():
    text = "this is a simple example"
    stopwords = {"is", "a"}
    clear_list = [word for word in text.split() if word not in stopwords]
    clear_text = " ".join(clear_list)
    print(clear_text)


if __name__ == "__main__":
    main()
