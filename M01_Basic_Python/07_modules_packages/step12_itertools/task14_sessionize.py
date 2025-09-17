from datetime import datetime
from itertools import groupby

events = [
    ("u1", "2025-09-16T10:00:00"),
    ("u1", "2025-09-16T10:10:00"),
    ("u1", "2025-09-16T11:00:00"),
    ("u1", "2025-09-16T11:20:00"),
    ("u2", "2025-09-16T09:00:00"),
    ("u2", "2025-09-16T09:40:00"),
    ("u2", "2025-09-16T10:50:00"),
    ("u3", "2025-09-16T12:00:00"),
]

timeout = 30


def group_events_by_user(users_events: list[tuple[str, str]]) -> dict[str, list[datetime]]:
    grouping_dict = {}
    for user, group in groupby(
        sorted(users_events, key=lambda x: (x[0], x[1])), key=lambda item: item[0]
    ):
        grouping_dict[user] = [datetime.fromisoformat(item[-1]) for item in group]
    return grouping_dict


def read_sessions(user_group: dict[str, list[datetime]]):
    for user, timestamps in user_group.items():
        sessions = []
        cur = []
        prev = None

        for ts in timestamps:
            if not cur:
                cur.append(ts)
                prev = ts
            else:
                difference = (ts - prev).total_seconds() / 60
                if difference > timeout:
                    sessions.append(cur)
                    cur = [ts]
                else:
                    cur.append(ts)
                prev = ts

        if cur:
            sessions.append(cur)

        user_group[user] = sessions
    return user_group


def main():
    group = group_events_by_user(events)
    data = read_sessions(group)
    for user, sessions in data.items():
        for idx, sess in enumerate(sessions, 1):
            times = [dt.strftime("%H:%M") for dt in sess]
            print(f"user={user} session={idx} events={times}")


if __name__ == "__main__":
    main()
