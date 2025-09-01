from datetime import datetime, timedelta, timezone


def main():
    utc = datetime.now(timezone.utc)

    tz_riga = timezone(timedelta(hours=3))
    riga_time = datetime.now(tz=tz_riga)

    print(f"UTC: {utc}")
    print(f"Riga: {riga_time}")


if __name__ == "__main__":
    main()
