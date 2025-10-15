import pytest
from tasks.task14_optional_leak import length_safe


@pytest.mark.parametrize(
    "string, expected", [("abc", 3), ("", 0), (None, 0), ("12345", 5), (" ", 1)]
)
def test_length_safe(string, expected):
    assert length_safe(string) == expected
