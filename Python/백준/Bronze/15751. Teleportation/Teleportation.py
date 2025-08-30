a, b, x, y = map(int, input().split())
if a > b:
    a, b = b, a
print(min(b-a, abs(a-x) + abs(b-y), abs(a-y) + abs(b-x)))
