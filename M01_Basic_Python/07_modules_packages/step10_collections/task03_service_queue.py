from collections import deque
from datetime import datetime


def main():
    dq = deque()
    commands = {
        "/help": "Output of all commands",
        "/arrive": "Add client on the right",
        "/serve": "Delete the client on the left and display his name",
        "/peek": "Show first client name without deleting",
        "/size": "Display the number of clients in the queue",
        "/clear": "Clear queue",
        "/show": "Show the entire queue",
        "/end": "Terminate program execution",
    }

    print("To view available commands, write: /help")
    while True:
        user_input = input("Enter command: ")

        match user_input:
            case "/help":
                print("\n--------------All commands--------------")
                for command, info in commands.items():
                    print(f"{command} - {info}")
                print("----------------------------------------\n")

            case "/arrive":
                name = input("What name to add: ")
                dq.append(name)

            case "/serve":
                if not dq:
                    print("Empty")
                else:
                    popped_name = dq.popleft()
                    print(popped_name)

            case "/peek":
                if dq:
                    print(f"The first client on the list: {dq[0]}")
                else:
                    print("Empty")

            case "/size":
                print(f"Total clients in queue: {len(dq)}")

            case "/clear":
                dq.clear()
                print("The queue is cleared!")

            case "/show":
                print("Queue:", ", ".join(dq) if dq else "Empty")

            case "/end":
                print(f"The program is complete [{datetime.now().strftime('%H:%M:%S')}]")
                break

            case _:
                print("Unknown command")


if __name__ == "__main__":
    main()
