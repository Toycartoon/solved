x, y = map(int, input().split())
v = 0
while y * v - x * v < y:
    v += 1

print(v)
