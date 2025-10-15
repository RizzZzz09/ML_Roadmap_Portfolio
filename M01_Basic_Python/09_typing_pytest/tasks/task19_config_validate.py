from typing import Dict

required = {
    "host": str,
    "port": int,
    "debug": bool,
}


def validate_config(cfg: Dict[str, object]) -> bool:
    for key, expected_type in required.items():
        if key not in cfg or not isinstance(cfg[key], expected_type):
            return False
    return True


def main() -> None:
    print(validate_config({"host": "localhost", "port": 8080, "debug": True}))
    print(validate_config({"host": "localhost", "port": "8080", "debug": True}))


if __name__ == "__main__":
    main()
