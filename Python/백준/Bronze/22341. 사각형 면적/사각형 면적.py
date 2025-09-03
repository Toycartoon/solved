import sys

input = sys.stdin.readline

n, c = map(int, input().split())
a, b = n, n
for i in range(c):
    x, y = map(int, input().split())
    if x >= a or y >= b:
        continue

    if x * b >= a * y:
        a = x
    else:
        b = y

print(a * b)
