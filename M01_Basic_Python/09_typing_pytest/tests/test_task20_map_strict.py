import pytest
from tasks.task20_map_strict import map_strict


@pytest.mark.parametrize(
    "item_list, func, expected",
    [
        ([1, 2, 3], lambda x: x * 2, [2, 4, 6]),
        ([], lambda x: x + 1, []),
        (["a", "bb"], len, [1, 2]),
        ([2, -2], lambda x: (1 / x), [0.5, -0.5]),
    ],
)
def test_map_strict(item_list, func, expected):
    assert map_strict(item_list, func) == expected


def test_map_strict_raises():
    with pytest.raises(ZeroDivisionError):
        map_strict([1, 0, 2], lambda x: 10 // x)
