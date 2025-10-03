import os
from contextlib import suppress

dir_path = "data/test_dir"


def create_dir(path: str):
    with suppress(FileExistsError):
        os.mkdir(path)


if __name__ == "__main__":
    create_dir(dir_path)
    create_dir(dir_path)
