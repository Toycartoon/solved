import sys

input = sys.stdin.readline

n, r, s = map(int, input().split())
for t in range(n):
    g = [input().strip() for _ in range(r)]
    p = 0

    for i in range(r):
        if "#" in g[i]:
            p = i
            break

    for i in range(r-1, -1, -1):
        if "#" in g[i]:
            print(abs(i-p))
            break
