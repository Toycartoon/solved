n, m = map(int, input().split())
a, d = map(int, input().split())
sr, sc = map(int, input().split())
g = [[False for _ in range(m)] for __ in range(n)]
g[sr-1][sc-1] = True

f = True
for y in range(n):
    if y == 0:
        if d == 1:
            for x in range(a-1, m):
                if g[y][x]:
                    f = False
                    break
        elif d == 0:
            for x in range(a):
                if g[y][x]:
                    f = False
                    break
    elif y == n-1:
        if d == 1:
            for x in range(m):
                if g[y][x]:
                    f = False
                    break
        else:
            if g[-1][-1]:
                f = False
                break
    else:
        for x in range(m):
            if g[y][x]:
                f = False
                break
    if d == 0:
        d = 1
    else:
        d = 0

if f:
    print("YES!")
else:
    print("NO...")
