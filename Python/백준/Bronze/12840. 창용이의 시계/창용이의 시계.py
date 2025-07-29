from datetime import datetime as dt, timedelta as td
import sys

input = sys.stdin.readline

ans = dt.strptime(input().strip(), "%H %M %S")
for q in range(int(input())):
    t, *c = map(int, input().split())

    if t == 1:
        ans += td(seconds=c[0])
    elif t == 2:
        ans += td(seconds=-c[0])
    elif t == 3:
        print(*map(int, dt.strftime(ans, "%H %M %S").split()))
