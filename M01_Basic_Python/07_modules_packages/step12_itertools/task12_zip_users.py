from itertools import zip_longest
from typing import Iterable, Iterator

ids_path = "data/ids.csv"
names_path = "data/names.csv"
output = "data/output.csv"


def file_reader(file: str) -> Iterator[str]:
    with open(file, "r", encoding="utf-8") as file:
        next(file)
        for line in file:
            line = line.strip()
            if not line:
                continue
            yield line.replace(";", ",").split(",", 1)[0]


def zipped_csv(first_file: str, second_file: str, fill: str = "-") -> Iterator[tuple[str, str]]:
    return zip_longest(file_reader(first_file), file_reader(second_file), fillvalue=fill)


def csv_save(path: str, data: Iterable[tuple[str, str]]):
    with open(path, "w", encoding="utf-8", newline="") as file:
        file.write("id,name\n")
        for id_line, name_line in data:
            file.write(f"{id_line},{name_line}\n")


def main():
    data = zipped_csv(ids_path, names_path)
    csv_save(output, data)


if __name__ == "__main__":
    main()
