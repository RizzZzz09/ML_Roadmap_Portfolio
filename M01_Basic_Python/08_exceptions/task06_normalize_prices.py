file_path = "data/prices.csv"


class DataFormatError(Exception):
    """Ошибка. Отсутствует столбец с ценой."""

    pass


class DataQualityError(Exception):
    """Ошибка. Некорректное значение цены."""

    pass


def main():
    not_correct_prices = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = file.read()
            data_list = data.replace("\n", " ").split(" ")
            for line, data in enumerate(data_list[1:], 1):
                product = data.split(",")[0].strip()
                price = data.split(",")[-1].strip()

                if not price.strip('"'):
                    raise DataFormatError(f"The product '{product}' has no price")

                if not price.isdigit():
                    not_correct_prices.append((line, price))

            if not_correct_prices:
                raise DataQualityError("Incorrect price value")

    except DataQualityError as error:
        print(error)
        for price in not_correct_prices:
            print(f"String {price[0]} - {price[-1]}")
    except DataFormatError as error:
        print(error)


if __name__ == "__main__":
    main()
