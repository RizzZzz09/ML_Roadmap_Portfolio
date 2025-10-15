from dataclasses import dataclass, field


@dataclass(frozen=True)
class Note:
    title: str
    tags: list[str] = field(default_factory=list)


def has_any_tag(n: Note, wanted: set[str]) -> bool:
    if not n.tags or not wanted:
        return False
    return bool(set(n.tags) & wanted)


def main() -> None:
    note = Note("A", ["ml", "python"])
    print(has_any_tag(note, {"ml"}))


if __name__ == "__main__":
    main()
