from itertools import combinations, combinations_with_replacement, permutations


def main():
    print(list(permutations("abc", 2)))
    print(list(combinations("abc", 2)))
    print(list(combinations_with_replacement("abc", 2)))


if __name__ == "__main__":
    main()
