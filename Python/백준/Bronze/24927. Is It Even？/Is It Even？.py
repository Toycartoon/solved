import sys

input = sys.stdin.readline

n, k = map(int, input().split())
f = False
a = 0
for i in range(n):
    v = int(input())
    while v % 2 == 0:
        a += 1
        v //= 2

    if a >= k:
        f = True
        break

print(int(f))
