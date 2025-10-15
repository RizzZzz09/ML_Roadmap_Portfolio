import pytest
from tasks.task02_word_counts import word_counts


@pytest.mark.parametrize(
    "text, expected",
    [
        ("hi hi bye", {"hi": 2, "bye": 1}),
        ("  one   two  one ", {"one": 2, "two": 1}),
        ("", {}),
        ("Hello hello HELLO", {"hello": 3}),
        ("hi, hi, hi, Hello ! ", {"hi": 3, "hello": 1}),
    ],
)
def test_word_counts(text, expected):
    assert word_counts(text) == expected
