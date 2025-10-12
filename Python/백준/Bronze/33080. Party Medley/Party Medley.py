from itertools import combinations as comb

n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
s = 0
for x in comb(a, 3):
    v = max(x)-min(x)
    if v <= m:
        s = max(s, sum([*x]))
        ans += 1

if ans == 0:
    print(-1)
else:
    print(ans, s)
