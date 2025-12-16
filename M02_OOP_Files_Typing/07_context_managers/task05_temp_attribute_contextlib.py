from contextlib import contextmanager
from typing import Iterator, TypeVar

T = TypeVar("T")
V = TypeVar("V")
_MISSING = object()


class Obj:
    def __init__(self) -> None:
        self.debug = False


@contextmanager
def temp_attribute(obj: T, attr_name: str, value: V) -> Iterator[T]:
    old_value = _MISSING
    has_attr = False

    if hasattr(obj, attr_name):
        has_attr = True
        old_value = getattr(obj, attr_name)

    setattr(obj, attr_name, value)

    try:
        yield obj
    finally:
        if has_attr:
            setattr(obj, attr_name, old_value)
        else:
            delattr(obj, attr_name)


def main() -> None:
    obj = Obj()

    with temp_attribute(obj, "debug", True):
        print(obj.debug)

    print(obj.debug)


if __name__ == "__main__":
    main()
