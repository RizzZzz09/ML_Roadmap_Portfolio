import argparse
import json
from datetime import datetime, timezone

from .core import operations
from .utils import storage


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

    args = parser.parse_args()

    fmt = args.format
    storage.ensure_history_file(fmt)
    path = storage.get_history_path(fmt)
    history = storage.load_history(path, fmt=fmt)

    if args.clear_history:
        history = []
        storage.save_history(history, path, fmt=fmt)
        print(json.dumps(history, ensure_ascii=False, indent=2))
        return

    if args.operation:
        if len(args.operands) != 2:
            print("Ошибка: нужно указать ровно 2 числа.")
            return

        a = parse_number(args.operands[0])
        b = parse_number(args.operands[1])
        if a is None or b is None:
            print("Ошибка: операнды должны быть числами.")
            return

        if args.operation == "div" and b == 0:
            print("Ошибка: деление на ноль.")
            return

        if args.operation == "add":
            result = operations.add(a, b)
        elif args.operation == "sub":
            result = operations.sub(a, b)
        elif args.operation == "mul":
            result = operations.mul(a, b)
        elif args.operation == "div":
            result = operations.div(a, b)

        entry = {
            "operation": args.operation,
            "operands": [a, b],
            "result": result,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        history.append(entry)
        storage.save_history(history, path, fmt=fmt)

    if args.show_history:
        print(json.dumps(history, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
