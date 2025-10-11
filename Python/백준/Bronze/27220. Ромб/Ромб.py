n = int(input())
a = int(input())
b = int(input())

g = [["." for _ in range(n)] for __ in range(n)]
k = n // 2
for y in range(n):
    for x in range(n):
        if a <= abs(k-y) + abs(k-x) <= b:
            g[y][x] = "*"

for i in g:
    print(*i, sep="")
