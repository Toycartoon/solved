from itertools import combinations as comb

n, h = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))

ans = float('inf')
for i in range(1, n+1):
    for v in comb(a, i):
        if sum(v) >= h:
            ans = min(ans, abs(h-sum(v)))
print(ans)
