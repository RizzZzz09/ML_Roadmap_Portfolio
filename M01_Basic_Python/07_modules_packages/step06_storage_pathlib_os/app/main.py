import argparse

from .core.operations import add, div, mul, sub
from .utils.printer import printer
from .utils.storage import ensure_data_dir, ensure_history_file, get_data_dir, get_history_path


def parse_number(value: str):
    """Пытается преобразовать строку в число (int или float)."""
    if value.lstrip("-").isdigit():
        return int(value)
    try:
        return float(value)
    except ValueError:
        return None


def main():
    parser = argparse.ArgumentParser(description="CLI-калькулятор")
    parser.add_argument("op", choices=["add", "sub", "mul", "div"], help="Операция")
    parser.add_argument("a", help="Первое число")
    parser.add_argument("b", help="Второе число")
    parser.add_argument("-v", "--verbose", action="store_true", help="Подробный вывод")
    parser.add_argument(
        "--history-dir", type=str, default=None, help="Пользовательский путь к каталогу хранения"
    )
    parser.add_argument(
        "--show-history-path",
        action="store_true",
        help="Показать путь к истории и завершить работу",
    )

    args = parser.parse_args()

    data_dir = get_data_dir(flag_path=args.history_dir)
    status = ensure_data_dir(data_dir)
    if isinstance(status, str):
        printer(status)
        return

    history_path = get_history_path(data_dir)
    status = ensure_history_file(history_path)
    if isinstance(status, str):
        printer(status)
        return

    if args.show_history_path:
        printer(history_path.resolve())
        return

    # Конвертируем аргументы
    a = parse_number(args.a)
    b = parse_number(args.b)

    if a is None or b is None:
        printer(f"Неверный ввод: {args.a}, {args.b}. Ожидались числа.")
        return

    operations = {
        "add": add,
        "sub": sub,
        "mul": mul,
        "div": div,
    }
    func = operations.get(args.op)

    if args.verbose:
        printer(f"[INFO] op={args.op} a={a} b={b}")

    result = func(a, b)
    printer(result)


if __name__ == "__main__":
    main()
