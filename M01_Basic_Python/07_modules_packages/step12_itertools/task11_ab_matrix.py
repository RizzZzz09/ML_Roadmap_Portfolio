from itertools import islice, product

options = {
    "theme": ["light", "dark"],
    "layout": ["new", "legacy"],
    "region": ["eu", "us", "apac"],
    "ab_slot": ["A", "B"],
}

rules = [
    ("theme=dark", "layout=legacy"),
    ("region=eu", "ab_slot=B"),
    ("layout=legacy", "ab_slot=B"),
]

combination = []
m = 10


def parse_cond(canon: list[tuple[str, str]]) -> list[tuple[str, str]]:
    rules_list = []
    for pair in canon:
        k1, v1 = pair[0].split("=")
        k2, v2 = pair[1].split("=")
        rules_list.append(((k1, v1), (k2, v2)))
    return rules_list


def violates(cfg: dict[str, str], rule: tuple[tuple[str, str], tuple[str, str]]) -> bool:
    (k1, v1), (k2, v2) = rule
    return cfg[k1] == v1 and cfg[k2] == v2


def main():
    keys = list(options.keys())
    values = list(options.values())
    stop_combinations = parse_cond(rules)

    for combo in product(*values):
        cfg = dict(zip(keys, combo, strict=False))
        if not any(violates(cfg, r) for r in stop_combinations):
            combination.append(cfg)

    result = list(islice(combination, 0, m))

    for cfg in result:
        print(",".join(f"{k}={cfg[k]}" for k in keys))


if __name__ == "__main__":
    main()
