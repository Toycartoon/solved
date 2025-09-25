a, b, c, x, y = map(int, input().split())
if a + b <= c * 2:
    print(a * x + b * y)
else:
    mn = min(x, y)
    s = mn * c * 2
    x -= mn
    y -= mn
    s += min(a * x + b * y, c * 2 * (x + y))
    print(s)
