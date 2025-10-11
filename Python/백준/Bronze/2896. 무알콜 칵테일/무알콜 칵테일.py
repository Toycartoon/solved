a, b, c = map(int, input().split())
i, j, k = map(int, input().split())
v = min(a / i, b / j, c / k)
print(a - i * v, b - j * v, c - k * v)
