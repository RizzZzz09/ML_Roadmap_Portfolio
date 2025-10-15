from collections import defaultdict
from typing import Callable, Dict, List, TypeVar

T = TypeVar("T")
K = TypeVar("K")


def group_by(xs: List[T], key: Callable[[T], K]) -> Dict[K, List[T]]:
    grouped_by_func = defaultdict(list)
    for value in xs:
        sorting_element = key(value)
        grouped_by_func[sorting_element].append(value)

    return dict(grouped_by_func)


def main() -> None:
    group = ["a", "bb", "ccc", "dd"]
    sorted_group = group_by(group, len)
    print(sorted_group)


if __name__ == "__main__":
    main()
