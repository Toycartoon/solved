n = int(input())
g = [[*input()] for _ in range(n)]
ans = [["" for _ in range(n)] for __ in range(n)]
for y in range(n):
    for x in range(n):
        if g[y][x].isnumeric():
            ans[y][x] = "*"
            continue

        a = 0
        for r in range(max(y-1, 0), min(y+2, n)):
            for c in range(max(x-1, 0), min(x+2, n)):
                if g[r][c].isnumeric():
                    a += int(g[r][c])

        if a >= 10:
            ans[y][x] = "M"
        else:
            ans[y][x] = a

for i in ans:
    print(*i, sep="")
