import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
ps = [[0 for _ in range(n+1)] for __ in range(n+1)]

for y in range(1, n+1):
    for x in range(1, n+1):
        ps[y][x] = ps[y-1][x] + ps[y][x-1] - ps[y-1][x-1] + a[y-1][x-1]

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(ps[x2][y2] - ps[x1-1][y2] - ps[x2][y1-1] + ps[x1-1][y1-1])
