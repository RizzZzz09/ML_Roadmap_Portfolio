def save_div(a: float, b: float) -> float | None:
    if b != 0:
        return a / b
    return None


def main() -> None:
    a, b = 5, 5
    print(save_div(a, b))


if __name__ == "__main__":
    main()
