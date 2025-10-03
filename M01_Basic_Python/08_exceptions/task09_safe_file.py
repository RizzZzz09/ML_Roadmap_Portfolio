file_pass = "data/missing.txt"


def safe_open(path: str):
    file = None
    try:
        file = open(path, "r", encoding="utf-8")
    except FileNotFoundError:
        raise
    else:
        return file.read()
    finally:
        if file is not None:
            file.close()


def main():
    try:
        data = safe_open(file_pass)
    except FileNotFoundError as error:
        print(f"Error: {error}")
    else:
        print(data)


if __name__ == "__main__":
    main()
