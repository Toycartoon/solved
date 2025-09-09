from datetime import datetime as dt, timedelta as td

t = dt.strptime(input(), "%H %M")
t -= td(minutes=int(input()))
t4t5 = dt.strptime(input(), "%H %M")
t -= td(hours=t4t5.hour, minutes=t4t5.minute)
br = int(input())
t6 = int(input())
t -= td(minutes=10 + (br + 1) * t6)

print(str(t.hour).zfill(2), str(t.minute).zfill(2))
