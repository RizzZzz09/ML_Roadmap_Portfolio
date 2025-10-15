import os
from typing import List

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

file_path = os.path.join(DATA_DIR, "output.txt")


def save_lines(path: str, lines: List[str]) -> bool:
    if not path:
        return False

    dir_name = os.path.dirname(path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)

    try:
        with open(path, "w", encoding="utf-8") as file:
            for line in lines:
                file.write(line + "\n")
        return True
    except OSError as error:
        print(f"File error: {error}")
        return False


def main() -> None:
    lines = ["a", "b", "c"]
    print(save_lines(file_path, lines))


if __name__ == "__main__":
    main()
