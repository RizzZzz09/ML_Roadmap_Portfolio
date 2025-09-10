from collections import defaultdict


def main():
    data = {
        "Alice": ("Sales", 3000),
        "Bob": ("Sales", 3900),
        "Charlie": ("IT", 5200),
        "Diana": ("HR", 4100),
        "Eve": ("IT", 4800),
        "Frank": ("HR", 3900),
    }

    groups = defaultdict(list)

    for name, (dept, _salary) in data.items():
        groups[dept].append(name)

    print("[GROUPS]")
    for dept in sorted(groups):
        print(f"{dept}: {', '.join(groups[dept])}")

    avg = defaultdict(list)

    for _name, (dept, salary) in data.items():
        avg[dept].append(salary)

    print("[AVG]")
    for dept in sorted(avg):
        salaries = avg[dept]
        mean = sum(salaries) / len(salaries)
        print(f"{dept}: {mean:.2f}")


if __name__ == "__main__":
    main()
