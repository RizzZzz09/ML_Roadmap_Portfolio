from dataclasses import dataclass, field


@dataclass
class Report:
    date: str = "unknown"
    stats: dict[str, float] = field(default_factory=dict)


def main() -> None:
    first_report = Report()
    first_report.date = "today"
    first_report.stats["accuracy"] = 0.95
    print(first_report)

    second_record = Report()
    print(second_record)


if __name__ == "__main__":
    main()
