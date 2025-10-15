import pytest
from tasks.task05_apply_all import add, mul, sub


@pytest.mark.parametrize(
    "a, b, func_list, expected",
    [
        (3, 2, [add, sub, mul], [5, 1, 6]),
        (10, 5, [sub, mul], [5, 50]),
        (2, 3, [add], [5]),
        (4, 4, [], []),
    ],
)
def test_apply_all(a, b, func_list, expected):
    pass
