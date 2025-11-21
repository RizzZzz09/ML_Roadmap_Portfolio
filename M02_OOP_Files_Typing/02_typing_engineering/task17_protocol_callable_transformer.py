from typing import Protocol, TypeVar

T = TypeVar("T")


class Transformer(Protocol[T]):
    def transform(self, value: T) -> T: ...


class UpperCaseTransformer:
    def transform(self, value: str) -> str:
        return value.upper()


class MultiplyTransformer:
    def __init__(self, factor: int):
        self.factor: int = factor

    def transform(self, value: int) -> int:
        return value * self.factor


def apply(transformer: Transformer[T], value: T) -> T:
    return transformer.transform(value)


def main() -> None:
    t1 = UpperCaseTransformer()
    result = apply(t1, "hello")
    print(result)

    t2 = MultiplyTransformer(10)
    res = apply(t2, 3)
    print(res)


if __name__ == "__main__":
    main()
