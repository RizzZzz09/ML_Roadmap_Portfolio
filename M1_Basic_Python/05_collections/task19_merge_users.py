def main():
    users1 = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
    users2 = [{"id": 2, "age": 30}, {"id": 3, "name": "Carol"}]

    result = {}

    for user in users1 + users2:
        uid = user["id"]
        if uid not in result:
            result[uid] = {}
        result[uid].update(user)

    print(list(result.values()))


if __name__ == "__main__":
    main()
