from math import gcd
import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if len(set(a)) == 1:
        print("INFINITY")
    else:
        v = []
        for i in range(n):
            for j in range(i+1, n):
                v.append(abs(a[i]-a[j]))
        print(gcd(*v))
