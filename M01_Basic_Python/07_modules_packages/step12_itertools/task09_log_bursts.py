from itertools import groupby


def is_5xx(status: str) -> bool:
    return status.isdigit() and status.startswith("5")


def stream():
    with open("data/sample.log", "r", encoding="utf-8") as file:
        for index, line in enumerate(file, 1):
            status = line.rsplit(maxsplit=1)[-1].strip()
            yield index, is_5xx(status)


def main():
    for key_is_err, group_iter in groupby(stream(), lambda t: t[1]):
        if not key_is_err:
            continue

        first = None
        last = None
        count = 0

        for line, _ in group_iter:
            if first is None:
                first = line
            count += 1
            last = line

        if count > 0:
            print(f"start = {first}, end = {last}, count = {count}")


if __name__ == "__main__":
    main()
