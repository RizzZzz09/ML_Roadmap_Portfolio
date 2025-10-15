from typing import List, TypedDict


class UserID(TypedDict):
    id: int
    name: str
    tags: List[str]


def user_has_tag(user: UserID, need_tag: str) -> bool:
    return need_tag in user["tags"]


def main() -> None:
    user: UserID = {"id": 1, "name": "A", "tags": ["ml", "python"]}
    print(user_has_tag(user, "ml"))


if __name__ == "__main__":
    main()
