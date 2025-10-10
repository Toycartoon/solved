f = []
for i in range(int(input())):
    x, y = map(int, input().split())
    f.append((x, y))

ans = (0, 0)
rss = float('inf')
for a in range(1, 101):
    for b in range(1, 101):
        v = 0
        for x, y in f:
            v += (y - (a*x + b)) ** 2

        if rss > v:
            rss = v
            ans = (a, b)
print(*ans)
