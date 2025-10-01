from itertools import combinations as comb

n, s = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(1, n+1):
    for x in comb(a, i):
        if sum(x) == s:
            ans += 1
print(ans)
