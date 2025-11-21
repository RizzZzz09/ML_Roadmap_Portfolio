from typing import NewType, TypedDict

UserId = NewType("UserId", int)
OrderId = NewType("OrderId", int)


class UserBase(TypedDict):
    user_id: int
    name: str
    email: str


class OrderBase(TypedDict):
    order_id: int
    amount: int
    status: str


def load_user(user_id: UserId) -> UserBase:
    user: UserBase = {"user_id": user_id, "name": "Danil", "email": "task10@gmail.com"}

    return user


def load_order(order_id: OrderId) -> OrderBase:
    order: OrderBase = {"order_id": order_id, "amount": 100, "status": "paid"}

    return order


def main() -> None:
    user_id = UserId(1)
    order_id = OrderId(2)

    res_user = load_user(user_id)
    print(res_user)

    res_order = load_order(order_id)
    print(res_order)


if __name__ == "__main__":
    main()
