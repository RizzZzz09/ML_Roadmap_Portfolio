import os
from typing import List

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

file_path = os.path.join(DATA_DIR, "text.txt")


def read_lines(path: str) -> List[str] | None:
    try:
        with open(path, "r", encoding="utf-8") as file:
            return [line.strip() for line in file]
    except OSError:
        return None


def main() -> None:
    result = read_lines(file_path)
    print(result)


if __name__ == "__main__":
    main()
