import pytest
from tasks.task18_inverse import inverse


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1, 2, 4], [1.0, 0.5, 0.25]),
        ([0, 5], [None, 0.2]),
        ([], []),
        ([-1, 2], [-1.0, 0.5]),
        ([10, -10, 0], [0.1, -0.1, None]),
    ],
)
def test_inverse(numbers, expected):
    assert inverse(numbers) == expected
