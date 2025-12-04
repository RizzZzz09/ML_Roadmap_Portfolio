from dataclasses import dataclass


@dataclass(frozen=True)
class AppConfig:
    name: str
    version: str


def main() -> None:
    app = AppConfig("Test", "1.1.1.1")
    print(app)


"""
    try:
        app.version = "2.2.2.2"
    except FrozenInstanceError as error:
        print(f"Ошибка: {error}")
"""

if __name__ == "__main__":
    main()
