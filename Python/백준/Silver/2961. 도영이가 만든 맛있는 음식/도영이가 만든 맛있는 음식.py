from itertools import combinations as comb

a = []
n = int(input())
for i in range(n):
    s, b = map(int, input().split())
    a.append((s, b))

ans = float('inf')
for r in range(1, n+1):
    for i in comb(a, r):
        sour, bitter = 1, 0
        for v in i:
            sour *= v[0]
            bitter += v[1]
        ans = min(ans, abs(sour-bitter))

print(ans)
