from datetime import datetime as dt

while True:
    d, m, y = map(int, input().split())
    if d == m == y == 0:
        break

    try:
        dt(day=d, month=m, year=y)
        print("Valid")
    except ValueError:
        print("Invalid")
