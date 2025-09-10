from collections import Counter
from random import choices, seed


def main():
    seed(123)
    text = (
        "Python is great for data science and machine learning."
        "Data is the new oil, and Python helps to extract it."
        "Machine learning with Python is powerful and fun."
    )

    words_only = "".join(char.lower() for char in text if char.isalnum() or char.isspace())
    words_only_list = words_only.split(" ")

    counter = Counter(words_only_list)
    population = list(counter.keys())
    weights = list(counter.values())

    random_choices = choices(population, weights=weights, k=10_000)

    observed = Counter(random_choices)

    total = sum(counter.values())
    expected = {w: c / total for w, c in counter.items()}

    empirical = {w: observed[w] / 10_000 for w in expected}

    print("word    expected   empirical   diff")
    for word, _count in counter.most_common(10):
        e = expected[word]
        o = empirical[word]
        diff = o - e
        print(f"{word:8} {e:.4f}    {o:.4f}    {diff:+.4f}")


if __name__ == "__main__":
    main()
