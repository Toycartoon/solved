import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
infection = list(map(int, input().split()))

v = [False for _ in range(n)]
for i in infection:
    v[i-1] = True

g = []
for i in range(m):
    t, a, b = map(int, input().split())
    g.append((t, a, b))
g.sort()

for r in infection:
    ans = [False for _ in range(n)]
    ans[r-1] = True

    for _, a, b in g:
        if ans[a-1]:
            ans[b-1] = True

    if ans == v:
        print(r)
        break
