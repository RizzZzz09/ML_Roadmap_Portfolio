import pytest
from tasks.task01_normalize import normalize


@pytest.mark.parametrize(
    "inp, expected",
    [
        (["", " ", "Hi", "  PY  "], ["hi", "py"]),
        ([], []),
        (["Hello", " world "], ["hello", "world"]),
    ],
)
def test_normalize(inp, expected):
    assert normalize(inp) == expected
