import random


def main():
    data = [1, 2, 3, 4, 5]
    b = 10_000
    random.seed(123)
    bootstrap_sample_list = [random.choices(data, k=len(data)) for _ in range(b)]
    means = [sum(value) / len(value) for value in bootstrap_sample_list]

    means_sorted = sorted(means)
    lo = means_sorted[int(0.025 * b)]
    hi = means_sorted[int(0.975 * b)]

    sample_mean = sum(data) / len(data)
    print(f"n={len(data)}, B={b}")
    print(f"sample_mean={sample_mean:.4f}")
    print(f"ci95=[{lo:.4f}, {hi:.4f}]")


if __name__ == "__main__":
    main()
