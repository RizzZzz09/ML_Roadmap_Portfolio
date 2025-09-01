from datetime import datetime


def main():
    text = "31-12-2025 23:59"
    datetime_object = datetime.strptime(text, "%d-%m-%Y %H:%M")
    print(f"Year: {datetime_object.year}")
    print(f"Month: {datetime_object.month}")
    print(f"Day: {datetime_object.day}")
    print(f"Hour: {datetime_object.hour}")
    print(f"Minute: {datetime_object.minute}")


if __name__ == "__main__":
    main()
