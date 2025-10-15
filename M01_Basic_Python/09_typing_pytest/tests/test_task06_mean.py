import pytest


@pytest.mark.parametrize(
    "number_list, expected",
    [
        ([1, 2, 3], 2.0),
        ([1.5, 2.5, 3.5], 2.5),
        ([], None),
        ([2, 3.5], 2.75),
        ([10], 10.0),
    ],
)
def test_mean(number_list, expected):
    pass
