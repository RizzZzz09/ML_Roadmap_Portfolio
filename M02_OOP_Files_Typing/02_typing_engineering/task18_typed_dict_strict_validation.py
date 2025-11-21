from typing import NotRequired, TypedDict, Union


class InvalidProduct(Exception):
    """Ошибка. Выбрасывается, если продукта нет базовых ключей."""

    pass


class InvalidValue(Exception):
    """Ошибка. Выбрасывается, значение ключа словаря имеет не корректный тип данных."""

    pass


class ProductBase(TypedDict):
    id: int
    title: str
    price: float


class ProductDetails(ProductBase):
    description: NotRequired[str]
    category: NotRequired[str]
    tags: NotRequired[list[str]]


class ProductPublic(ProductBase):
    pass


def build_public_product(data: dict[str, Union[int, str, float, list[str]]]) -> ProductPublic:
    if not all(key in data for key in ("id", "title", "price")):
        raise InvalidProduct("Некорректный продукт.")

    raw_id = data["id"]
    if not isinstance(raw_id, int):
        raise InvalidValue('Некорректное значение поля "id", ожидалось значение "int".')

    raw_title = data["title"]
    if not isinstance(raw_title, str):
        raise InvalidValue('Некорректное значение ключа "title", ожидалось значение "str".')

    raw_price = data["price"]
    if not isinstance(raw_price, float):
        raise InvalidValue('Некорректное значение ключа "price", ожидалось значение "float".')

    public_product: ProductPublic = {"id": raw_id, "title": raw_title, "price": raw_price}

    return public_product


def main() -> None:
    data: dict[str, int | str | float | list[str]] = {
        "id": 1,
        "title": "Laptop",
        "price": 999.99,
        "description": "...",
        "tags": ["tech"],
    }

    try:
        result = build_public_product(data)
    except (InvalidProduct, InvalidValue) as error:
        print(f"> {error}")
    else:
        print(result)


if __name__ == "__main__":
    main()
