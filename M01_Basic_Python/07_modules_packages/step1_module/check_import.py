import math_utils


def main():
    result = math_utils.add(2, 2)
    print(result)

    result = math_utils.sub(10, 5)
    print(result)

    result = math_utils.mul(4, 4)
    print(result)

    result = math_utils.div(10, 2)
    print(result)

    result = math_utils.div(10, 0)
    print(result)

    result = math_utils.add_list([1, 2, 3, 4, 5], [1, 2])
    print(result)


if __name__ == "__main__":
    main()
