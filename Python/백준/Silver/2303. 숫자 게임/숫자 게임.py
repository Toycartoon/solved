from itertools import combinations as comb

n = int(input())
a = []
for _ in range(n):
    l = list(map(int, input().split()))
    mx = 0
    for c in comb(l, 3):
        mx = max(mx, sum(c) % 10)
    a.append((mx, _+1))

a.sort()
print(a[-1][1])
