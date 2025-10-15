import pytest
from tasks.task15_save_lines import save_lines


@pytest.mark.parametrize(
    "lines, expected",
    [
        (["a", "b", "c"], True),
        ([], True),
    ],
)
def test_save_lines_success(tmp_path, lines, expected):
    path = tmp_path / "test_output.txt"

    result = save_lines(str(path), lines)

    assert result is expected
    if lines:
        content = path.read_text(encoding="utf-8")
        assert content == "\n".join(lines) + "\n"
    else:
        assert path.read_text(encoding="utf-8") == ""


def test_save_lines_nested_dir(tmp_path):
    nested_path = tmp_path / "subdir" / "nested.txt"

    result = save_lines(str(nested_path), ["x"])

    assert result is True
    assert nested_path.exists()
    assert nested_path.read_text(encoding="utf-8") == "x\n"


def test_save_lines_empty_path():
    result = save_lines("", ["data"])
    assert result is False


def test_save_lines_oserror(tmp_path):
    dir_path = tmp_path / "subdir"
    dir_path.mkdir()

    result = save_lines(str(dir_path), ["will fail"])
    assert result is False
