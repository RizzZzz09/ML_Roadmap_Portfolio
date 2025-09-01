from datetime import datetime


def main():
    now = datetime.now()
    ts = int(now.timestamp())
    from_ts = datetime.fromtimestamp(ts)

    print(f"Now: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Timestamp: {ts}")
    print(f"From timestamp: {from_ts.strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    main()
