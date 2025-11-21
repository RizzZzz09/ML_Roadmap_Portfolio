from typing import Any, Final, NotRequired, Required, TypedDict

REQUIRED_FIELDS: Final[list[str]] = ["id", "user_name", "email"]


class InvalidProfile(Exception):
    """Ошибка. Выбрасывается, если у пользователя нет базовых ключей."""

    pass


class UserBase(TypedDict):
    """Базовая модель пользователя."""

    id: Required[int]
    user_name: Required[str]
    email: Required[str]


class UserPublic(UserBase):
    """Публичная модель пользователя. Наследуется от UserBase."""

    name: Required[str]
    surname: Required[str]
    patronymic: NotRequired[str]
    avatar_url: NotRequired[str]


def build_profile(data: dict[str, Any]) -> UserPublic:
    # Проверка обязательных ключей профиля
    for key in REQUIRED_FIELDS:
        if key not in data:
            raise InvalidProfile(f'Формат пользователя неверный. Отсутствует ключ "{key}"')

    user_public: UserPublic = {
        "id": data["id"],
        "user_name": data["user_name"],
        "email": data["email"],
        "name": data["name"],
        "surname": data["surname"],
    }

    if "patronymic" in data:
        user_public["patronymic"] = data["patronymic"]

    if "avatar_url" in data:
        user_public["avatar_url"] = data["avatar_url"]

    return user_public


def main() -> None:
    data = {
        "id": 1,
        "user_name": "RizzZzz",
        "email": "abc123@gmail.com",
        "name": "Danil",
        "surname": "Ivanov",
        "avatar_url": "qwerty",
    }

    try:
        result = build_profile(data)
    except InvalidProfile as error:
        print(f"> {error}")
    else:
        for key, value in result.items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    main()
