import pytest
from tasks.task03_shift import shift


@pytest.mark.parametrize(
    "points, dx, dy, expected",
    [
        ([(0, 0), (1, 2)], 1, -1, [(1, -1), (2, 1)]),
        ([], 5, 5, []),
        ([(2, 3)], -2, -3, [(0, 0)]),
        ([(1, 1), (-1, -1)], 0, 10, [(1, 11), (-1, 9)]),
    ],
)
def test_shift(points, dx, dy, expected):
    assert shift(points, dx, dy) == expected
