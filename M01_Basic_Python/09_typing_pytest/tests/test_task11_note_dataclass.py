import pytest
from tasks.task11_note_dataclass import Note, has_any_tag


@pytest.mark.parametrize(
    "note, wanted, expected",
    [
        (Note("A", ["ml", "python"]), {"ml"}, True),
        (Note("B", []), {"ml"}, False),
        (Note("C", ["ML"]), {"ml"}, False),
        (Note("D", ["data", "python"]), set(), False),
        (Note("E", ["py", "ml", "dl"]), {"dl"}, True),
    ],
)
def test_has_any_tags(note, wanted, expected):
    assert has_any_tag(note, wanted) == expected
