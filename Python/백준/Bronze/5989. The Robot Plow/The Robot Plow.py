x, y, i = map(int, input().split())
g = [[False for _ in range(x)] for __ in range(y)]

for _ in range(i):
    xll, yll, xur, yur = map(int, input().split())
    for r in range(yll-1, yur):
        for c in range(xll-1, xur):
            g[r][c] = True

ans = 0
for r in range(y):
    for c in range(x):
        if g[r][c]:
            ans += 1
print(ans)
