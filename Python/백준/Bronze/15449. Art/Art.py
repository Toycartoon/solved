from itertools import combinations as comb

l = list(map(int, input().split()))
ans = 0
for a, b, c in comb(l, 3):
    if a + b > c and a + c > b and b + c > a:
        ans += 1
print(ans)
