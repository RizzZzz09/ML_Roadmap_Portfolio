from collections import Counter
from typing import Dict


def word_counts(text: str) -> Dict[str, int]:
    words_only = "".join([char for char in text if char.isalnum() or char.isspace()])
    return dict(Counter([word.lower() for word in words_only.split()]))


def main() -> None:
    text = "hi, hi, hi, Hello ! "
    result = word_counts(text)
    print(result)


if __name__ == "__main__":
    main()
