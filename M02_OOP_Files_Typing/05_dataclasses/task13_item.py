import time
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Item:
    id: int
    value: int
    timestamp: str = field(compare=False)


def main() -> None:
    first_item = Item(1223, 12, datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
    time.sleep(2)
    second_item = Item(1223, 12, datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    print(first_item)
    print(second_item)

    print(first_item == second_item)


if __name__ == "__main__":
    main()
