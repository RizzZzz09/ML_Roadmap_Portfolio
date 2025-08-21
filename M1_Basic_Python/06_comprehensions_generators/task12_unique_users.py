def main():
    logs = ["user1:actionA", "user2:actionB", "user1:actionC", "user3:actionA"]
    unique_users = {user.split(":", 1)[0] for user in logs}
    print(unique_users)


if __name__ == "__main__":
    main()
