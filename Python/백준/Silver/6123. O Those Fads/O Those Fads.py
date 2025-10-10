import sys

input = sys.stdin.readline

n, l, k = map(int, input().split())
r = []
for i in range(n):
    r.append(int(input()))

r.sort()
ans = 0
for i in r:
    if l >= i:
        ans += 1
        l += k
    else:
        break
print(ans)
