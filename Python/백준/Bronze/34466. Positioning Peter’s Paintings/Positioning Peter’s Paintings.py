a, b, x, y = map(int, input().split())
s = min(a + 2 * b + x + 2 * y + abs(a - x), a * 2 + b + x * 2 + y + abs(b - y))
print(s)