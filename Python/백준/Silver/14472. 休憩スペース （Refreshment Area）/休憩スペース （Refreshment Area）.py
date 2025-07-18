n, m, d = map(int, input().split())
g = [[*input()] for _ in range(n)]

ans = 0
for y in range(n):
    for x in range(d, m+1):
        if g[y][x-d:x].count("#") == 0:
            ans += 1

for x in range(m):
    for y in range(d, n+1):
        if list(zip(*g))[x][y-d:y].count("#") == 0:
            ans += 1

print(ans)
