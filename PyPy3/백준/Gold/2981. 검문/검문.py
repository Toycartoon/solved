from math import gcd
import sys

input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

v = []
for i in range(1, n):
    v.append(abs(a[i]-a[i-1]))
m = gcd(*v)
ans = []
for i in range(2, m+1):
    if m % i == 0:
        ans.append(i)
print(*ans)
