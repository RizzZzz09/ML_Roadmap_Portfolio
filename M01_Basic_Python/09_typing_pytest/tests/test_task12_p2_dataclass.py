import pytest
from tasks.task12_p2_dataclass import P2, translate


@pytest.mark.parametrize(
    "points, dx, dy, expected",
    [
        ([P2(0, 0), P2(2, 2)], 1, -1, [P2(1, -1), P2(3, 1)]),
        ([], 5, 5, []),
        ([P2(2, 3)], -2, -3, [P2(0, 0)]),
        ([P2(1, 1), P2(-1, -1)], 0, 10, [P2(1, 11), P2(-1, 9)]),
    ],
)
def test_translate(points, dx, dy, expected):
    assert translate(points, dx, dy) == expected
