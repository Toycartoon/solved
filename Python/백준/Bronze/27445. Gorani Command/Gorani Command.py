n, m = map(int, input().split())
a = []
for i in range(n-1):
    a.append((i+1, 1, int(input())))

v = list(map(int, input().split()))
for i in range(m):
    a.append((n, i+1, v[i]))

for y in range(1, n+1):
    for x in range(1, m+1):
        f = True
        for r, c, d in a:
            if abs(r-y) + abs(c-x) != d:
                f = False
                break

        if f:
            print(y, x)
            exit()
