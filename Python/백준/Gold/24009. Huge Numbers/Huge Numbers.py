from math import factorial as f
import sys

input = sys.stdin.readline

for t in range(int(input())):
    a, n, p = map(int, input().split())
    print(f"Case #{t+1}: {pow(a, f(n), p)}")
