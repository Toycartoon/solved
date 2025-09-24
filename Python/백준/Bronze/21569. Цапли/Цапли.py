from math import ceil

a, b = map(int, input().split())
print(ceil(max(a, b) / 2), min(a, b))
