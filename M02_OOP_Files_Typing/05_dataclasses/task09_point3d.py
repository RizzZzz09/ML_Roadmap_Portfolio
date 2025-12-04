from dataclasses import dataclass


@dataclass(slots=True)
class Point3D:
    x: float
    y: float
    z: float


def main() -> None:
    point = Point3D(1, 2, 3)
    print(point)

    try:
        print(point.__dict__)
    except AttributeError as error:
        print(f"> Ошибка. {error}")


"""
    try:
        point.w = 10
    except AttributeError as error:
        print(f"> Ошибка при добавлении атрибута: {error}")
"""

if __name__ == "__main__":
    main()
