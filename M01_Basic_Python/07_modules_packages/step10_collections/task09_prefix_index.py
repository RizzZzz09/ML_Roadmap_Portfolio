from collections import defaultdict


def main():
    groups = defaultdict(list)

    while True:
        user_input = input("Enter a word: ").strip()
        if user_input.upper() == "END":
            break

        if not user_input:
            continue
        if not user_input[0].isalpha():
            continue

        groups[user_input[0].lower()].append(user_input.lower())

    for letter in sorted(groups):
        words = sorted(set(groups[letter]))
        quoted = ", ".join(f'"{w}"' for w in words)
        print(f"{letter}: [{quoted}]")


if __name__ == "__main__":
    main()
