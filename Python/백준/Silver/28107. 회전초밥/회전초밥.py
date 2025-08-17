import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
a = [deque() for _ in range(200001)]
for i in range(n):
    k, *s = map(int, input().split())
    for v in s:
        a[v].append(i)

b = list(map(int, input().split()))
ans = [0 for _ in range(n)]

for i in b:
    if len(a[i]) > 0:
        ans[a[i].popleft()] += 1

print(*ans)
