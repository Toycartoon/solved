from math import inf
import sys

input = sys.stdin.readline

l, r, u, d = inf, -inf, -inf, inf
for i in range(int(input())):
    x, y, c = input().split()
    if c == "L":
        l = min(l, int(x))
    elif c == "R":
        r = max(r, int(x))
    elif c == "U":
        u = max(u, int(y))
    elif c == "D":
        d = min(d, int(y))

if (abs(l-r)-1) * (abs(u-d)-1) == inf:
    print("Infinity")
else:
    print((abs(l-r)-1) * (abs(u-d)-1))
