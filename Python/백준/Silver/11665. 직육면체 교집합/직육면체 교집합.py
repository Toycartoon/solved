n = int(input())
x = (0, 1001)
y = (0, 1001)
z = (0, 1001)

for i in range(n):
    x1, y1, z1, x2, y2, z2 = map(int, input().split())
    x = (max(x[0], x1), min(x[1], x2))
    y = (max(y[0], y1), min(y[1], y2))
    z = (max(z[0], z1), min(z[1], z2))

if x[1] <= x[0] or y[1] <= y[0] or z[1] <= z[0]:
    print(0)
else:
    print((x[1]-x[0]) * (y[1] - y[0]) * (z[1] - z[0]))
