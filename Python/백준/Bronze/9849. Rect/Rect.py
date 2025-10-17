n = int(input())
x = (0, 10000)
y = (0, 10000)

for i in range(n):
    x1, x2, y1, y2 = map(int, input().split())
    x = (max(x[0], x1), min(x[1], x2))
    y = (max(y[0], y1), min(y[1], y2))

if x[1] <= x[0] or y[1] <= y[0]:
    print(0)
else:
    print((x[1]-x[0]) * (y[1] - y[0]))
