from datetime import date, timedelta


def main():
    now = date.today()
    print(f"In 7 days: {now + timedelta(days=7)}")
    print(f"In 30 days: {now + timedelta(days=30)}")
    print(f"In 365 days: {now + timedelta(days=365)}")


if __name__ == "__main__":
    main()
