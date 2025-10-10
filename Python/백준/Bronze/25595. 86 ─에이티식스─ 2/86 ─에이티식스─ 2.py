n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
x, y = -1, -1
for r in range(n):
    for c in range(n):
        if g[r][c] == 2:
            x, y = c, r
            break

f = True
for r in range(n):
    for c in range(n):
        if g[r][c] == 1:
            if (abs(y-r) + abs(x-c)) % 2 == 0:
                f = False
                break

if f:
    print("Lena")
else:
    print("Kiriya")
