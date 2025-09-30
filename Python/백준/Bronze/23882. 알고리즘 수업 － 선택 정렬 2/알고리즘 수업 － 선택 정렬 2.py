import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

idx = 0
for x in range(n-1, 0, -1):
    t = max(a[:x+1])
    if a[x] < t:
        v = a.index(t)
        a[v], a[x] = a[x], a[v]
        idx += 1

        if idx == k:
            print(*a)
            exit()
print(-1)
