from typing import NotRequired, TypedDict


class UserBase(TypedDict):
    id: int
    email: str


class UserPublic(UserBase):
    name: NotRequired[str]
    avatar_url: NotRequired[str]


class UserInternal(UserBase):
    is_admin: bool
    last_login_ts: NotRequired[int]


def make_public(user: UserInternal) -> UserPublic:
    public_info: UserPublic = {"id": user["id"], "email": user["email"]}
    return public_info


def main() -> None:
    user: UserInternal = {
        "id": 1,
        "email": "abc@gmail.com",
        "is_admin": True,
        "last_login_ts": 1700000,
    }

    result = make_public(user)
    print(result)


if __name__ == "__main__":
    main()
