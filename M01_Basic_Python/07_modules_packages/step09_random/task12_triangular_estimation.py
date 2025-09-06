import random


def main():
    minimum_time = 5
    most_likely_time = 7
    maximum_time = 12
    dead_line = 10

    b = 50_000

    time_list = [random.triangular(minimum_time, maximum_time, most_likely_time) for _ in range(b)]
    success = sum(1 for t in time_list if t <= dead_line)
    probability = success / b

    print(f"n = {b}")
    print(f"P(X <= {dead_line}) = {probability:.4f}")


if __name__ == "__main__":
    main()
