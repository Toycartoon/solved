from math import ceil

n = int(input())
k = ceil(n ** 0.5)
print((k-1) * 2 + (ceil(n / k)-1) * 2 if n > 2 else 4)
