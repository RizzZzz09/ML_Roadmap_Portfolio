from collections import OrderedDict

HELP_TEXT = """\
LRU Cache CLI
Commands:
  cap   - set capacity (>=1)
  put   - insert/update key/value (marks as fresh)
  get   - read value by key (marks as fresh or prints MISS)
  show  - print cache from oldest to freshest: k1=v1, k2=v2, ...
  help  - show this help
  end   - exit
"""


def main():
    cache = OrderedDict()
    capacity = None

    print("LRU Cache CLI. Type 'help' to see commands.")
    while True:
        cmd = input("> ").strip().lower()
        if not cmd:
            continue

        if cmd == "help":
            print(HELP_TEXT)

        elif cmd == "cap":
            while True:
                new_capacity = input("Specify storage capacity: ").strip()

                # Проверка на число
                if not new_capacity.isdigit():
                    print("Storage capacity must be a number")
                    continue

                # Проверка на величину
                if int(new_capacity) < 1:
                    print("Storage capacity cannot be less than 1")
                    continue
                break

            capacity = int(new_capacity)

            while len(cache) > capacity:
                cache.popitem(last=False)

        elif cmd == "put":
            if not capacity:
                print("First you need to specify the storage size!")
                continue

            key = input("Enter key: ").strip()
            value = input("Enter value: ").strip()

            if not key or not value:
                print("Key and value cannot be empty!")
                continue

            if key in cache:
                cache[key] = value
                cache.move_to_end(key, last=True)
            else:
                if len(cache) == capacity:
                    cache.popitem(last=False)
                cache[key] = value

        elif cmd == "get":
            if not capacity:
                print("First you need to specify the storage size!")
                continue

            key = input("Enter key: ").strip()

            if not key:
                print("Key cannot be empty!")
                continue

            if key in cache:
                print(f"{key} - {cache[key]}")
                cache.move_to_end(key, last=True)
            else:
                print("MISS")

        elif cmd == "show":
            if capacity is None:
                print("First you need to specify the storage size!")
                continue

            if cache:
                print(", ".join(f"{k}={v}" for k, v in cache.items()))
            else:
                print("(empty)")

        elif cmd == "end":
            print("Bye!")
            break

        else:
            print("Unknown command. Type 'help'.")


if __name__ == "__main__":
    main()
