from typing import Literal, NotRequired, Protocol, TypedDict


class InvalidMethod(Exception):
    """Ошибка. Выбрасывается, если пользователь вызвал метод, которого нет."""

    pass


class Request(TypedDict):
    method: Literal["GET", "POST"]
    path: str
    query: NotRequired[dict[str, str]]
    body: NotRequired[str]


class Response(TypedDict):
    status_code: int
    body: str


class Handler(Protocol):
    def handle(self, request: Request) -> Response: ...


class UsersHandler:
    def handle(self, request: Request) -> Response:
        if request["method"] == "GET":
            if request["path"] == "/users":
                return {"status_code": 200, "body": "users list"}
            else:
                return {"status_code": 404, "body": "empty"}

        elif request["method"] == "POST":
            if request["path"] == "/users":
                return {"status_code": 200, "body": "user created"}
            else:
                return {"status_code": 404, "body": "empty"}

        else:
            raise InvalidMethod(f'Метод "{request["method"]}" не поддерживается программой.')


class OrdersHandler:
    def handle(self, request: Request) -> Response:
        if request["method"] == "GET":
            if request["path"] == "/orders":
                return {"status_code": 200, "body": "orders list"}
            else:
                return {"status_code": 404, "body": "empty"}

        elif request["method"] == "POST":
            if request["path"] == "/orders":
                return {"status_code": 200, "body": "order created"}
            else:
                return {"status_code": 404, "body": "empty"}

        else:
            raise InvalidMethod(f'Метод "{request["method"]}" не поддерживается программой.')


def route_request(request: Request, handlers: dict[str, Handler]) -> Response:
    path = request["path"]

    for prefix, handler in handlers.items():
        if path.startswith(prefix):
            return handler.handle(request)

    return {"status_code": 404, "body": "no handler for path"}


def main() -> None:
    handlers: dict[str, Handler] = {
        "/users": UsersHandler(),
        "/orders": OrdersHandler(),
    }

    req1: Request = {"method": "GET", "path": "/users"}
    req2: Request = {"method": "POST", "path": "/orders"}
    req3: Request = {"method": "GET", "path": "/unknown"}

    print(route_request(req1, handlers))
    print(route_request(req2, handlers))
    print(route_request(req3, handlers))


if __name__ == "__main__":
    main()
