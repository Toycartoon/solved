import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

mx = []
for i in range(n):
    mx.append(max(a[i]))

ans = []
for i in range(m):
    v = 0
    for j in range(n):
        if mx[j] != a[j][i]:
            v += 1
    ans.append(v)
print(*ans)
