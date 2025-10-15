import pytest
from tasks.task13_missing_return import save_div


@pytest.mark.parametrize(
    "a, b, expected", [(10, 2, 5.0), (3, 0, None), (-9, 3, -3.0), (0, 1, 0.0), (5, -2, -2.5)]
)
def test_save_div(a, b, expected):
    assert save_div(a, b) == expected
