from math import ceil

n, x = map(int, input().split())
a = list(map(int, input().split()))

ans = (sum(a) - x * n) / (x - 100)
print(max(ceil(ans), 0))
