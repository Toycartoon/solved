import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = []
for i in range(n):
    t, g = map(int, input().split())
    a.append((t, g))

a.sort(key=lambda x: (x[0], -x[1]))
ans = 0
for t, g in a:
    if m - t >= 0:
        m -= t
        ans += g
    else:
        break

print(ans)
