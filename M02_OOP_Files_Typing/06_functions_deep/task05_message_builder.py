from typing import Protocol, cast


class MessageBuilder(Protocol):
    def add(self, message: str) -> "MessageBuilder": ...

    def finish(self) -> str: ...


def build_message(prefix: str) -> MessageBuilder:
    parts: list[str] = []

    def builder() -> None:
        return None

    def add(message: str) -> MessageBuilder:
        parts.append(message)
        return cast(MessageBuilder, builder)

    def finish() -> str:
        return f"{prefix}: " + "; ".join(parts)

    builder.add = add
    builder.finish = finish

    return cast(MessageBuilder, builder)


def main() -> None:
    msg = build_message("INFO")

    result = msg.add("user logged in").add("id=42").add("status=ok").finish()

    print(result)


if __name__ == "__main__":
    main()
