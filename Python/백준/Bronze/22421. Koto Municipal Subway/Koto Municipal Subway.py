import sys
from math import inf

input = sys.stdin.readline

while True:
    d, e = map(int, input().split())
    if d == e == 0:
        break

    ans = inf
    for y in range(d):
        x = d - y
        ans = min(ans, abs((x ** 2 + y ** 2) ** 0.5 - e))

    print(ans)
