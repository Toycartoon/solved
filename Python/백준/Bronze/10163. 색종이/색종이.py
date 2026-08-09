import sys

input = sys.stdin.readline

a = [[-1 for _ in range(1001)] for __ in range(1001)]
n = int(input())
ans = [0 for _ in range(n)]
for i in range(n):
    _x, _y, w, h = map(int, input().split())
    for x in range(_x, _x+w):
        for y in range(_y, _y+h):
            a[y][x] = i

for y in range(1001):
    for x in range(1001):
        if a[y][x] != -1:
            ans[a[y][x]] += 1

for v in ans:
    print(v)
