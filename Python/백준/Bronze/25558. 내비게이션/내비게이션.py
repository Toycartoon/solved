n = int(input())
sx, sy, ex, ey = map(int, input().split())
a = []
for _ in range(n):
    x, y = sx, sy
    d = 0
    for i in range(int(input())):
        xi, yi = map(int, input().split())
        d += abs(x-xi) + abs(y-yi)
        x, y = xi, yi

    d += abs(x-ex) + abs(y-ey)
    a.append(d)

print(a.index(min(a))+1)
