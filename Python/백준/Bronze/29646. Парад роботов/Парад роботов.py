import sys

input = sys.stdin.readline

n, k = map(int, input().split())
x = []
y = []
sx, sy = 0, 0
for i in range(n):
    u, v = map(int, input().split())
    x.append(u)
    y.append(v)
    sx += u
    sy += v

for i in range(k):
    px = sx / n
    py = sy / n

    sx = sx - x[i] + px
    sy = sy - y[i] + py
    x[i] = px
    y[i] = py

print(x[k-1], y[k-1])
