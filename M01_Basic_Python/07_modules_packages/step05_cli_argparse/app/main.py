import argparse

from .core.operations import add, div, mul, sub
from .utils.printer import printer


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

    args = parser.parse_args()

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
