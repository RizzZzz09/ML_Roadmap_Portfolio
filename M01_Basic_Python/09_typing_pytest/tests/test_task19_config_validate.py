import pytest
from tasks.task19_config_validate import validate_config


@pytest.mark.parametrize(
    "config, expected",
    [
        ({"host": "localhost", "port": 8080, "debug": True}, True),
        ({"host": "127.0.0.1", "port": 5000, "debug": False}, True),
        ({"host": "localhost", "port": "8080", "debug": True}, False),
        ({"host": "localhost", "port": 8080}, False),
        ({}, False),
    ],
)
def test_validate_config(config, expected):
    assert validate_config(config) == expected
