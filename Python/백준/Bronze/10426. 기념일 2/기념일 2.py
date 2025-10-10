from datetime import datetime as dt, timedelta as td

n, k = input().split()
t = dt.strptime(n, "%Y-%m-%d") + td(days=int(k)-1)
print(dt.strftime(t, "%Y-%m-%d"))
