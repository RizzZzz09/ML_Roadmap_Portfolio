from datetime import datetime


def main():
    now = datetime.now()
    new_year = datetime(now.year + 1, 1, 1)
    number_of_days_until_new_year = new_year - now
    print(f"Days until New Year: {number_of_days_until_new_year.days}")


if __name__ == "__main__":
    main()
