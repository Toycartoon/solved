from math import gcd
import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

v = []
for i in range(1, n):
    v.append(abs(a[i]-a[i-1]))
print(gcd(*v))
