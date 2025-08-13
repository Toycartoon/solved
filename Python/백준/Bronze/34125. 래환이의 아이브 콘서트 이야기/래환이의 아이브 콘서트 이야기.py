n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

ans = float('inf')
i, j = -1, -1

for r in range(n):
    for c in range(m):
        if g[r][c] == 0 and (r+1) + abs((m + 1) / 2 - (c + 1)) < ans:
            ans = (r+1) + abs((m + 1) / 2 - (c + 1))
            i, j = r+1, c+1

if i == j == -1:
    print(-1)
else:
    print(i, j)
