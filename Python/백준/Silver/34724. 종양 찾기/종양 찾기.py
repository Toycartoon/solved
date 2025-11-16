n, m = map(int, input().split())
g = [[*input()] for _ in range(n)]

f = True
for y in range(n-1):
    for x in range(m-1):
        if g[y][x] == g[y+1][x] == g[y][x+1] == g[y+1][x+1] == "1":
            f = False
            break
print(int(not f))
