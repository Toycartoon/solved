import sys
from math import log, sin, sqrt, trunc, e

input = sys.stdin.readline

x = [1]
for i in range(1, 1000001):
    x.append((x[trunc(i-sqrt(i))] + x[trunc(log(i, e))] + x[trunc(i * sin(i) ** 2)]) % 1000000)

while True:
    n = int(input())
    if n == -1:
        break
    print(x[n])
