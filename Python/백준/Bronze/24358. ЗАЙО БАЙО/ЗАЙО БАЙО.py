from datetime import datetime as dt, timedelta as td

x, n = map(int, input().split())
d = (2 * x - 1) * n - 1
now = dt.strptime(input(), "%d %m %Y")
print(*map(int, dt.strftime(now + td(days=d), "%d %m %Y").split()))
