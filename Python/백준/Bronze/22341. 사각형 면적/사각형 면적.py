import sys

input = sys.stdin.readline

n, c = map(int, input().split())
a, b = n, n
for i in range(c):
    x, y = map(int, input().split())
    if x >= a or y >= b:
        continue

    if a * y >= x * b:
        b = y
    else:
        a = x

print(a * b)
