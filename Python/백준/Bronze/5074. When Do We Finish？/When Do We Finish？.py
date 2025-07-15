from datetime import datetime as dt, timedelta

while True:
    a, b = input().split()

    if a == b == "00:00":
        break

    a = dt.strptime(a, "%H:%M")
    h, m = map(int, b.split(":"))

    future = a + timedelta(hours=h, minutes=m)
    print(f"{str(future.hour).zfill(2)}:{str(future.minute).zfill(2)}" + (f" +{(future.day - a.day)}" if (future.day - a.day) > 0 else ""))
