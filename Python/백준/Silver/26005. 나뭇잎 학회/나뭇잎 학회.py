from math import ceil

n = int(input())
if n == 1:
    print(0)
else:
    print(ceil((n ** 2) / 2))
