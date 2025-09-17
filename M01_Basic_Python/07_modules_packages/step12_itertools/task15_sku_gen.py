import string
from itertools import islice, product
from typing import Iterable, Iterator

all_digits = string.digits
all_letters = string.ascii_uppercase


def parse_prefixes(prefixes_str: str) -> list[str]:
    return [p.strip().upper() for p in prefixes_str.split(",") if p.strip()]


def parse_limit(raw: str) -> int | None:
    raw = raw.strip()
    if not raw:
        return None
    value = int(raw)
    if value <= 0:
        print("Limit must be > 0")
    return value


def sku_generator(prefixes: Iterable[str], letters: str, digits: str) -> Iterator[str]:
    combos = product(prefixes, letters, letters, digits, digits)
    for p, l1, l2, d1, d2 in combos:
        yield f"{p}-{l1}{l2}{d1}{d2}"


def show_sku(sku_iter: Iterator[str], limit: int | None = None) -> None:
    it = sku_iter if limit is None else islice(sku_iter, limit)
    for code in it:
        print(code)


def main():
    prefix_input = input("What symbols to use: ")
    prefixes = parse_prefixes(prefix_input)
    if not prefixes:
        print("Нужно указать хотя бы один префикс, например: A,B,C")
        return

    generated_combos = sku_generator(prefixes, all_letters, all_digits)
    limit_input = input("How many codes to show: ")
    limit = parse_limit(limit_input)
    if not limit:
        show_sku(generated_combos)
    else:
        show_sku(generated_combos, limit)


if __name__ == "__main__":
    main()
