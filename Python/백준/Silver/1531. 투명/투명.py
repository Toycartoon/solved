n, m = map(int, input().split())
g = [[0 for _ in range(100)] for __ in range(100)]

for i in range(n):
    ldx, ldy, rux, ruy = map(int, input().split())
    for y in range(ldy-1, ruy):
        for x in range(ldx-1, rux):
            g[y][x] += 1

ans = 0
for y in range(100):
    for x in range(100):
        if g[y][x] > m:
            ans += 1

print(ans)
