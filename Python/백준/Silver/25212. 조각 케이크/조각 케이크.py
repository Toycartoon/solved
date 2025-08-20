from itertools import combinations as comb

n = int(input())
c = list(map(int, input().split()))

ans = 0
for r in range(1, n+1):
    for i in comb(c, r):
        a = 0
        for v in i:
            a += 1 / v

        if 0.99 <= a <= 1.01:
            ans += 1

print(ans)
