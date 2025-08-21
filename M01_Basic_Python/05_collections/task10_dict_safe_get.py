def main():
    user = {"name": "Alice", "age": 25}
    city = user.get("city", "Unknown")
    print(city)


if __name__ == "__main__":
    main()
