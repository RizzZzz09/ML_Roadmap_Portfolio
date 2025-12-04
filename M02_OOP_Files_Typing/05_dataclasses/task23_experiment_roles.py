from dataclasses import dataclass, field


@dataclass
class BaseExperiment:
    name: str
    tags: list[str] = field(default_factory=list)


@dataclass
class TaggedExperiment(BaseExperiment):
    description: str = "no description"


def main() -> None:
    tagger = TaggedExperiment("Test_two")
    tagger.tags.append("baseline")
    print(tagger)


if __name__ == "__main__":
    main()
