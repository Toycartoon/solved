from math import ceil

a, b, h = map(int, input().split())

ans = 1
h -= a
ans += max(0, ceil(h / (a - b)))
print(ans)
