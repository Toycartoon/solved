n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
k, l = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(k)]

ans = [[0 for _ in range(l)] for _ in range(n)]
for y in range(n):
    for x in range(l):
        v = 0
        for i in range(m):
            v += a[y][i] * b[i][x]
        ans[y][x] = v

for i in ans:
    print(*i)
