n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

ans = float('inf')
for y in range(n):
    for x in range(m):
        cost = 0
        for r in range(n):
            for c in range(m):
                cost += g[r][c] * (abs(y-r) + abs(x-c))
        ans = min(ans, cost)
print(ans)
