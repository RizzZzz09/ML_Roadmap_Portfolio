import random


def main():
    prizes = ["small", "medium", "jackpot"]
    weights = [0.7, 0.29, 0.01]
    n = 100_000

    random.seed(123)
    prize_draw = random.choices(prizes, k=n, weights=weights)
    counter_prize = {}

    for result in prize_draw:
        counter_prize[result] = counter_prize.get(result, 0) + 1

    print("prize     expected   empirical   diff")
    for i, prize in enumerate(prizes):
        exp = weights[i]
        emp = counter_prize[prize] / n
        diff = emp - exp
        sign = "+" if diff >= 0 else ""
        print(f"{prize:<9} {exp:<10.4f} {emp:<10.4f} {sign}{diff:.4f}")


if __name__ == "__main__":
    main()
