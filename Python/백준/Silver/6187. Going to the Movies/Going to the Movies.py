from itertools import combinations as comb

h, n = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))

ans = 0
for i in range(1, n+1):
    for v in comb(a, i):
        if sum(v) <= h:
            ans = max(ans, sum(v))
print(ans)
