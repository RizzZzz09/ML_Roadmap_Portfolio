import pytest
from tasks.task17_hello_capsys import print_hello


@pytest.mark.parametrize(
    "name, expected",
    [
        ("Danil", "Hello, Danil!\n"),
        ("world", "Hello, world!\n"),
        ("", "Hello, !\n"),
        ("ML", "Hello, ML!\n"),
    ],
)
def test_print_hello(capsys, name, expected):
    print_hello(name)
    captured = capsys.readouterr()
    assert captured.out == expected
