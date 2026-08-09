n, a, b, c, d, e, f, g, h = map(int, input().split())

ans = 0
v = []
for x in range(n+1):
    for y in range(n-x+1):
        z = n-x-y
        if z < 0:
            continue

        if a * x + b * y + c * z == d and e * x + f * y + g * z == h:
            ans += 1
            v.append((x, y, z))

if ans == 1:
    print(0)
    print(*v[0])
elif ans > 1:
    print(1)
else:
    print(2)
