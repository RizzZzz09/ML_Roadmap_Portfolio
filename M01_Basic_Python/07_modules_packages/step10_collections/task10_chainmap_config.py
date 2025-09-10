from collections import ChainMap


def parse_value(s: str):
    s = s.strip()
    if s.lstrip("-").isdigit():
        return int(s)
    return s


def format_kv(key: str, value):
    k = f'"{key}"'
    if isinstance(value, int):
        v = str(value)
    else:
        v = f'"{value}"'
    return f"{k}: {v}"


def main():
    system = {"theme": "light", "lang": "en", "timeout": 30}
    env = {"timeout": 20}
    user = {}

    while True:
        line = input("Enter configurations: ").strip()
        if not line:
            continue
        if line.upper() == "END":
            break
        if "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        user[key] = parse_value(value)

    final = ChainMap(user, env, system)

    keys = sorted(final.keys())
    body = ", ".join(format_kv(k, final[k]) for k in keys)
    result = "{" + body + "}"
    print(result)


if __name__ == "__main__":
    main()
