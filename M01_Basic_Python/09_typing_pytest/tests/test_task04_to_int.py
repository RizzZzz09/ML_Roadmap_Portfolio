import pytest
from tasks.task04_to_int import to_int


@pytest.mark.parametrize(
    "inp, expected",
    [
        ("42", 42),
        (" 7 ", 7),
        ("abc", None),
        ("", None),
        (" 3.14", None),
    ],
)
def test_to_int(inp, expected):
    assert to_int(inp) == expected
