import sys
from math import gcd

input = sys.stdin.readline

for i in range(int(input())):
    a, b = map(int, input().split())
    g = gcd(a, b)
    print(a // g, b // g)
