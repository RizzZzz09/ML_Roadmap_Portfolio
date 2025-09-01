from datetime import datetime


def format_datetime(dt_obj: datetime) -> str:
    return dt_obj.strftime("%d/%m/%Y, %H:%M")


if __name__ == "__main__":
    now = datetime.now()
    print(format_datetime(now))
