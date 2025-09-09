from math import trunc

x = list(map(int, input().split()))
n, kwf = map(int, input().split())

s = 0
for i in range(1, 10, 2):
    s += x[i-1] * x[i]

print(trunc(n * trunc(s / 5) / kwf))
