import pytest
from tasks.task10_point_namedtuple import Point, distance


@pytest.mark.parametrize(
    "first_point, second_point, expected",
    [
        (Point(0, 0), Point(3, 4), 5.0),
        (Point(1, 1), Point(1, 1), 0.0),
        (Point(-1, -1), Point(2, 3), 5.0),
        (Point(2.5, 1.5), Point(2.5, 4.5), 3.0),
    ],
)
def test_distance(first_point, second_point, expected):
    assert distance(first_point, second_point) == expected
