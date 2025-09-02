import sys

input = sys.stdin.readline

n, m = map(int, input().split())
v = []
for i in range(n):
    a, b = map(int, input().split())
    v.append((a, b))

for j in range(m):
    g, x, y = map(int, input().split())
    ans = 0
    for a, b in v:
        if x <= a and y <= b and a + b <= g:
            ans += 1
    print(ans)
