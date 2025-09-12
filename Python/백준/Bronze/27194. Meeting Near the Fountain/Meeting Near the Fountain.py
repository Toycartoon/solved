from math import ceil

n, t = map(int, input().split())
m = int(input())
x, y = map(int, input().split())

x *= 60
y *= 60

v = ceil((n - m) / y + m / x)
print(max(0, v - t))
