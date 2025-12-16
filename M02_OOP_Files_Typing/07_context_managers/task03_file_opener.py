from pathlib import Path
from types import TracebackType
from typing import IO, Union


class FileOpener:
    def __init__(self, file_path: Union[Path, str], mode: str) -> None:
        self.file_path = file_path
        self.mode = mode
        self._file: IO[str] | None = None

    def __enter__(self) -> IO[str]:
        self._file = open(self.file_path, self.mode)
        return self._file

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        if self._file is not None:
            self._file.close()


def main() -> None:
    with FileOpener("data/text.txt", "w") as file:
        file.write("Hello World")


if __name__ == "__main__":
    main()
