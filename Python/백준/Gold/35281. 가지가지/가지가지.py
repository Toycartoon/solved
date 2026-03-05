n, m = map(int, input().split())

if (n % 2 != m % 2) or n == 2 or m == 2:
    print(-1)
    exit()

g = [["." for _ in range(m)] for __ in range(n)]
g[0][-1] = "G"
g[1][-1] = "g"
g[-1][-2:] = ["G", "g"]

x, y = m-3, n-2
while y > 0 and x > 0:
    if y > x:
        g[y][x] = "G"
        g[y][x+1] = "g"
    else:
        g[y][x] = "G"
        g[y+1][x] = "g"
    y -= 1
    x -= 1

while x > 0 or y > 0:
    if x > 0:
        g[y][x] = "G"
        g[y+1][x] = "g"
        x -= 1

        if x == 0 and y == 0:
            g[y][x] = "G"
            g[y+1][x] = "g"
    elif y > 0:
        g[y][x] = "G"
        g[y][x+1] = "g"
        y -= 1

print(max(n, m))
for v in g:
    print(*v, sep="")
