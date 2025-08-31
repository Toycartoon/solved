x, y, d, t = map(int, input().split())
dist = ((x ** 2) + (y ** 2)) ** 0.5
ans = 0
if d / t <= 1:
    print(dist)
    exit()

while 2 * d < dist:
    ans += t
    dist -= d

ans += min(dist, 2 * t, t + abs(dist - d))
print(ans)
