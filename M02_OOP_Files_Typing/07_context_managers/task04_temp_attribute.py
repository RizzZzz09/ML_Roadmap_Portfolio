from types import TracebackType
from typing import Generic, TypeVar

V = TypeVar("V")
T = TypeVar("T")
_MISSING = object()


class TempAttribute(Generic[T, V]):
    def __init__(self, obj: T, attr_name: str, value: V) -> None:
        self._obj = obj
        self.attr_name = attr_name
        self.value = value

        self._has_attr: bool = False
        self._old_value: object = _MISSING

    def __enter__(self) -> T:
        if hasattr(self._obj, self.attr_name):
            self._has_attr = True
            self._old_value = getattr(self._obj, self.attr_name)

        setattr(self._obj, self.attr_name, self.value)
        return self._obj

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        if self._has_attr:
            setattr(self._obj, self.attr_name, self._old_value)
        else:
            delattr(self._obj, self.attr_name)
        return None


class Obj:
    def __init__(self) -> None:
        self.debug = False


def main() -> None:
    obj = Obj()

    with TempAttribute(obj, "debug", True):
        print(obj.debug)

    print(obj.debug)


if __name__ == "__main__":
    main()
