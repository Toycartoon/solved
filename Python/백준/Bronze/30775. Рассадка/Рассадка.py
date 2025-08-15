from math import ceil

m, k = map(int, input().split())
n = list(map(int, input().split()))
print(ceil(sum(n) / m))
