def main():
    a = {"Alice", "Bob", "Carol"}
    b = {"Bob", "Dave"}

    mutual_friends = set.intersection(a, b)
    friends_only_a = set.difference(a, b)
    all_friends = set.union(a, b)

    # mutual_friends = a & b
    # friends_only_a = a - b
    # all_friends = a | b

    print(mutual_friends)
    print(friends_only_a)
    print(all_friends)


if __name__ == "__main__":
    main()
