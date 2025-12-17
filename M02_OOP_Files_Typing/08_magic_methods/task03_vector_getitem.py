from typing import Sequence, Union

Numbers = Union[int, float]


class SimpleVector:
    def __init__(self, number_list: Sequence[Numbers]) -> None:
        self._number_list = number_list

    def __getitem__(self, index: int) -> Numbers:
        return self._number_list[index]


def main() -> None:
    number_list = [number for number in range(101)]

    vector = SimpleVector(number_list)
    print(vector[0])
    print(vector[-1])


if __name__ == "__main__":
    main()
