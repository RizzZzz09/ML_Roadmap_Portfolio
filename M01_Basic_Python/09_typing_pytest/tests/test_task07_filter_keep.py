import pytest
from tasks.task07_filter_keep import filter_keep


@pytest.mark.parametrize(
    "value_list, filter_func, expected",
    [
        ([1, 2, 3, 4], lambda v: v % 2 == 0, [2, 4]),
        (["a", "bb", "ccc"], lambda s: len(s) >= 2, ["bb", "ccc"]),
        ([], lambda _: True, []),
        ([0, 1, 2], bool, [1, 2]),
        ([True, False, True], lambda x: not x, [False]),
    ],
)
def test_filter_keep(value_list, filter_func, expected):
    assert filter_keep(value_list, filter_func) == expected
