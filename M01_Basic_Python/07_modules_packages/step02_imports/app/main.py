from core.operations import add, add_list, div, mul, sub
from utils.printer import printer

# from .core.operations import add, sub, mul, div, add_list
# from .utils.printer import printer


def main():
    result = add(2, 2)
    printer(result)

    result = sub(10, 5)
    printer(result)

    result = mul(4, 4)
    printer(result)

    result = div(10, 2)
    printer(result)

    result = div(10, 0)
    printer(result)

    result = add_list([1, 2, 3, 4, 5], [1, 2])
    printer(result)


if __name__ == "__main__":
    main()
