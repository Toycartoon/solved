import sys

input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    a.append(float(input()))

ans = 0
for i in range(n):
    f = 1
    for v in range(i, n):
        f *= a[v]
        ans = max(ans, f)

print(f"{ans:.03f}")
