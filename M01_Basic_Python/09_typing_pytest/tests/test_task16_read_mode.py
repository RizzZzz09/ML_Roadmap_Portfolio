import pytest
from tasks.task16_read_mode import read_lines


@pytest.mark.parametrize(
    "lines, expected",
    [
        ("hello", ["hello"]),
        ("", []),
        ("x\ny\r\nz\r\n", ["x", "y", "z"]),
        (" \n\t\nx \n", ["", "", "x"]),
    ],
)
def test_read_lines(tmp_path, lines, expected):
    path = tmp_path / "test_output.txt"
    path.write_text(lines, encoding="utf-8", newline="")
    assert read_lines(str(path)) == expected
