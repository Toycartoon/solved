from datetime import datetime as dt, timedelta as td

t = dt.strptime(input(), "%I:%M %p")
k = int(input())

t -= td(minutes=k)
s = t.strftime("%I:%M %p")
print(f"{int(s.split(":")[0])}:{s.split(':')[1]}")
