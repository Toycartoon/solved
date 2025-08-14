from math import ceil

n, s = map(int, input().split())
a = list(map(int, input().split()))
print(ceil((max(a) * s) / 1000))
