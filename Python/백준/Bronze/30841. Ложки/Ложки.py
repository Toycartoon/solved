a, b = map(int, input().split())
print(int(1 // ((1 / a) + (1 / b))) if a != 0 and b != 0 else 0)
