n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
w = {}
for y in range(n):
    for x in range(m):
        if a[y][x] in w:
            w[a[y][x]] += 1
        else:
            w[a[y][x]] = 1

odd = 0
for i in w.values():
    if i % 2 == 1:
        odd += 1

if m % 2 == 1:
    if 1 <= odd <= n or m == 1:
        print("YES")
    else:
        print("NO")
else:
    if odd != 0:
        print("NO")
    else:
        print("YES")
