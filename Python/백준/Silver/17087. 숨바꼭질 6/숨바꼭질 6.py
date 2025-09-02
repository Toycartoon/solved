from math import gcd

n, s = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
    a[i] -= s

print(gcd(*a))
