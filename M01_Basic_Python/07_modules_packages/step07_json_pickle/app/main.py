import argparse


def parse_number(value: str):
    """Преобразует строку в число (int или float)."""
    if value.lstrip("-").isdigit():
        return int(value)
    try:
        return float(value)
    except ValueError:
        return None


def main():
    parser = argparse.ArgumentParser(description="CLI калькулятор с историей операций")

    # Подкоманды для операций
    parser.add_argument(
        "operation",
        choices=["add", "sub", "mul", "div"],
        nargs="?",
        help="Операция: add, sub, mul, div",
    )
    parser.add_argument("operands", nargs="*", help="Операнды (числа)")

    # Флаги истории
    parser.add_argument(
        "--show-history",
        action="store_true",
        help="Показать историю операций",
    )
    parser.add_argument(
        "--clear-history",
        action="store_true",
        help="Очистить историю операций",
    )
    parser.add_argument(
        "--format",
        choices=["json", "pickle"],
        default="json",
        help="Формат хранения истории (по умолчанию json)",
    )

    args = parser.parse_args()  # noqa: F841

    # TODO: Step 7.2 — тут будет загрузка истории
    # TODO: Step 7.3 — тут будет выполнение операций
    # TODO: Step 7.4 — тут будет сохранение истории и вывод


if __name__ == "__main__":
    main()
