import pytest
from tasks.task08_group_by import group_by


@pytest.mark.parametrize(
    "list_values, func, expected",
    [
        (["a", "bb", "ccc", "dd"], len, {1: ["a"], 2: ["bb", "dd"], 3: ["ccc"]}),
        ([1, 2, 3, 4, 5], lambda x: x % 2, {1: [1, 3, 5], 0: [2, 4]}),
        ([], lambda x: x, {}),
        (["apple", "banana"], lambda s: s[0], {"a": ["apple"], "b": ["banana"]}),
    ],
)
def test_group_by(list_values, func, expected):
    assert group_by(list_values, func) == expected
