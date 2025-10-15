from typing import List


def normalize(words: List[str]) -> List[str]:
    return [word.strip().lower() for word in words if word.strip()]


def main() -> None:
    words_list = [" ", "", "Hi", " PY "]
    result = normalize(words_list)
    print(result)


if __name__ == "__main__":
    main()
