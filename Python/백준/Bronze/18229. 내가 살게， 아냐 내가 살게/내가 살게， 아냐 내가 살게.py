n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

v = [0 for _ in range(n)]
for y in range(m):
    for x in range(n):
        v[x] += a[x][y]
        if v[x] >= k:
            print(x+1, y+1)
            exit()
