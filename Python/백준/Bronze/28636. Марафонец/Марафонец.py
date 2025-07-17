from datetime import datetime as dt, timedelta as td

n = int(input())
ans = dt.strptime(input(), "%M:%S")
for i in range(n-1):
    m, s = map(int, input().split(":"))
    ans += td(minutes=m, seconds=s)

print(dt.strftime(ans, "%H:%M:%S"))
