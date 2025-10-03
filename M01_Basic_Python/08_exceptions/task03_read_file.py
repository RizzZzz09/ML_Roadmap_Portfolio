file_path = "data/text.txt"


def main():
    file = None
    try:
        file = open(file_path)
        data = file.readlines()
    except FileNotFoundError as error:
        print(f"Error: {error}")
    else:
        print(f"Total strings: {len(data)}")
    finally:
        file.close()


if __name__ == "__main__":
    main()
