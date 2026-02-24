n, m = map(int, input().split())
r, c, d = map(int, input().split())
r += 1
c += 1

def pos(d):
    if d == 0:
        return 0, -1
    elif d == 1:
        return 1, 0
    elif d == 2:
        return 0, 1
    else:
        return -1, 0

g = [[1 for _ in range(m+2)]]
for i in range(n):
    g.append([1] + list(map(int, input().split())) + [1])
g.append([1 for _ in range(m+2)])
dust = [[True for _ in range(m+2)] for __ in range(n+2)]

for y in range(n+2):
    for x in range(m+2):
        if g[y][x] == 1:
            dust[y][x] = False

ans = 0
while True:
    if dust[r][c]:
        dust[r][c] = False
        ans += 1

    if not (dust[r-1][c] or dust[r+1][c] or dust[r][c-1] or dust[r][c+1]):
        dc, dr = pos(d)
        if g[r-dr][c-dc] == 1:
            break
        else:
            r -= dr
            c -= dc
    else:
        d = (d-1) % 4
        dc, dr = pos(d)
        if g[r+dr][c+dc] == 0 and dust[r+dr][c+dc]:
            c += dc
            r += dr
print(ans)
