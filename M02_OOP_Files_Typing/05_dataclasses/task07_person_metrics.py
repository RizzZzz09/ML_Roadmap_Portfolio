from dataclasses import dataclass, field


@dataclass
class PersonMetrics:
    height_m: float
    weight_kg: float
    bmi: float = field(init=False)

    def __post_init__(self) -> None:
        self.bmi = round(self.weight_kg / pow(self.height_m, 2), 3)


def main() -> None:
    my_metrics = PersonMetrics(1.86, 88.0)
    print(my_metrics)


if __name__ == "__main__":
    main()
