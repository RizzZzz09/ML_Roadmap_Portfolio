from dataclasses import dataclass


@dataclass
class Worker:
    name: str
    base_salary: float

    def __post_init__(self) -> None:
        self.base_salary = round(self.base_salary, 2)


@dataclass
class Employee(Worker):
    bonus: float

    def __post_init__(self) -> None:
        super().__post_init__()
        self.bonus = round(self.bonus, 2)


def main() -> None:
    worker = Worker("Danil", 12000.011212)
    employee = Employee("Alina", 200222.21234212, 120.999)

    print(worker)
    print(employee)


if __name__ == "__main__":
    main()
