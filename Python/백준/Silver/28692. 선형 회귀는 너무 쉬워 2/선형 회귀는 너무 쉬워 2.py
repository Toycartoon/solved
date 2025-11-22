import sys

input = sys.stdin.readline

sx, sy, sxx, sxy = 0, 0, 0, 0
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    sx += x
    sy += y
    sxx += x ** 2
    sxy += x * y

try:
    a = (n * sxy - sx * sy) / (n * sxx - sx ** 2)
    b = (sy - a * sx) / n
    print(a, b)
except ZeroDivisionError:
    print("EZPZ")
