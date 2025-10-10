import sys

input = sys.stdin.readline

n = int(input())
t = [0 for i in range(n+1)]
for i in range(n * (n-1) // 2):
    a, b, c, d = map(int, input().split())
    if c > d:
        t[a] += 3
    elif c < d:
        t[b] += 3
    else:
        t[a] += 1
        t[b] += 1

v = sorted(t, reverse=True)
for i in range(1, len(t)):
    print(v.index(t[i])+1)
