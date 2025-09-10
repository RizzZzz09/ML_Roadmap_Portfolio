from collections import Counter


def main(text: str):
    return Counter(text).most_common(5)


if __name__ == "__main__":
    for element in main("hello world!!!"):
        print(f"{element[0]}\t{element[-1]}")
