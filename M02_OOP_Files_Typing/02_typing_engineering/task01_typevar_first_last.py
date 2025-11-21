from typing import Sequence, TypeVar

T = TypeVar("T")


def first(xs: Sequence[T]) -> T:
    return xs[0]


def last(xs: Sequence[T]) -> T:
    return xs[-1]


def main() -> None:
    names_list = ["Danil", "Kirill", "Mark", "David"]
    ages_list = [18, 21, 43, 10, 8]

    first_name_in_names_list = first(names_list)
    last_name_in_names_list = last(names_list)

    first_value_age_in_ages_list = first(ages_list)
    last_value_age_in_ages_list = last(ages_list)

    print(first_name_in_names_list)
    print(last_name_in_names_list)
    print(first_value_age_in_ages_list)
    print(last_value_age_in_ages_list)


if __name__ == "__main__":
    main()
