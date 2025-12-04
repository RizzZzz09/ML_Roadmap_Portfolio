from dataclasses import dataclass, field


@dataclass
class ExperimentConfig:
    seed: int = 42
    hyperparams: dict[str, float] = field(default_factory=dict)
    tags: list[str] = field(default_factory=list)


def main() -> None:
    first_config = ExperimentConfig()
    second_config = ExperimentConfig()

    first_config.hyperparams["lr"] = 0.001
    first_config.tags.append("baseline")

    print(first_config)
    print(second_config)


if __name__ == "__main__":
    main()
