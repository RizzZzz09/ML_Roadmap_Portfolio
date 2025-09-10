from collections import OrderedDict


def main():
    od = OrderedDict()

    while True:
        user_input = input("Enter the command: ").strip().lower()
        match user_input:
            case "set":
                key = input("Enter key: ")
                value = input("Enter value: ")
                od[key] = value

            case "move_first":
                key = input("Enter key: ")
                if key in od:
                    od.move_to_end(key, last=False)
                else:
                    print("Key not found")

            case "move_last":
                key = input("Enter key: ")
                if key in od:
                    od.move_to_end(key, last=True)
                else:
                    print("Key not found")

            case "pop_first":
                if od:
                    k, v = od.popitem(last=False)
                    print(f"{k}={v}")
                else:
                    print("EMPTY")

            case "pop_last":
                if od:
                    k, v = od.popitem(last=True)
                    print(f"{k}={v}")
                else:
                    print("EMPTY")

            case "show":
                print(", ".join(f"{k}={v}" for k, v in od.items()))

            case "end":
                break


if __name__ == "__main__":
    main()
