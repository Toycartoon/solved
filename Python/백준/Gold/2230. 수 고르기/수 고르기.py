import sys

input = sys.stdin.readline

a = []
n, m = map(int, input().split())
for i in range(n):
    a.append(int(input()))

a.sort()
ans = float('inf')
l, r = 0, 0
while l <= r:
    if r == len(a):
        break
    v = a[r]-a[l]
    if v >= m:
        ans = min(ans, v)
        if v == m:
            break
        l += 1
    else:
        r += 1
print(ans)
