n = int(input())
x1, y1, x2, y2 = map(int, input().split())
print((x2-x1) * 2 + (y2-y1) * 2)

for i in range(n-1):
    a, b, c, d = map(int, input().split())
    x1, y1, x2, y2 = min(a, x1), min(b, y1), max(c, x2), max(d, y2)
    print((x2-x1) * 2 + (y2-y1) * 2)
