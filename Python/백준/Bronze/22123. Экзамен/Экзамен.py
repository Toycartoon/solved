from datetime import datetime as dt, timedelta as td
import sys

input = sys.stdin.readline

for t in range(int(input())):
    a, b, k = input().split()
    s = dt.strptime(a, "%H:%M:%S")
    f = dt.strptime(b, "%H:%M:%S")
    if s >= f:
        f += td(days=1)

    if s + td(minutes=int(k)) <= f:
        print("Perfect")
    elif s + td(minutes=int(k)) > f + td(hours=1):
        print("Fail")
    else:
        print("Test")
