n, m = map(int, input().split())
g = [input() for _ in range(n)]

ans = 0
for y in range(n):
    for x in range(m):
        if g[y][x] == "X":
            if y > 0 and g[y-1][x] == "Y":
                ans += 1
            if y < n-1 and g[y+1][x] == "Y":
                ans += 1
            if x > 0 and g[y][x-1] == "Y":
                ans += 1
            if x < m-1 and g[y][x+1] == "Y":
                ans += 1
print(ans)
