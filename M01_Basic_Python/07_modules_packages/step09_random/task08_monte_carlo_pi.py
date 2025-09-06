import random


def estimate_pi(n: int, seed: int | None = None) -> float:
    if seed is not None:
        random.seed(seed)

    pairs = [(random.uniform(-1, 1), random.uniform(-1, 1)) for _ in range(n)]
    count_inside = sum([1 for x, y in pairs if x * x + y * y <= 1])
    return 4 * (count_inside / n)


if __name__ == "__main__":
    print(f"N = 1000    π ≈ {estimate_pi(1000, 123):.4f}")
    print(f"N = 10000   π ≈ {estimate_pi(10000, 123):.4f}")
    print(f"N = 100000  π ≈ {estimate_pi(100000, 123):.4f}")
