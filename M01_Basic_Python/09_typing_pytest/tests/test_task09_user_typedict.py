import pytest
from tasks.task09_user_typedict import user_has_tag


@pytest.mark.parametrize(
    "user, need_tag, expected",
    [
        ({"id": 1, "name": "A", "tags": ["ml", "python"]}, "ml", True),
        ({"id": 2, "name": "B", "tags": []}, "ml", False),
        ({"id": 3, "name": "C", "tags": ["ML"]}, "ml", False),
        ({"id": 4, "name": "D", "tags": ["data", "python"]}, "py", False),
        ({"id": 5, "name": "E", "tags": ["py", "ml", "dl"]}, "dl", True),
    ],
)
def test_user_has_tag(user, need_tag, expected):
    assert user_has_tag(user, need_tag) == expected
