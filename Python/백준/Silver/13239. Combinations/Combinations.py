import sys
from math import comb

input = sys.stdin.readline

for t in range(int(input())):
    n, k = map(int, input().split())
    print(comb(n, k) % 1000000007)
