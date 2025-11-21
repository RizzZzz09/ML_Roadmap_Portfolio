from typing import Callable, Concatenate, ParamSpec, TypeVar

D = TypeVar("D")
P = ParamSpec("P")


def with_context(func: Callable[P, D]) -> Callable[Concatenate[str, P], D]:
    def wrapper(context: str, /, *args: P.args, **kwargs: P.kwargs) -> D:
        print(f"[{context}]. Была вызвана функция {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@with_context
def greet(name: str) -> str:
    return f"Hello, {name}!"


def main() -> None:
    name = "Danil"
    result = greet("TEST", name)
    print(result)


if __name__ == "__main__":
    main()
