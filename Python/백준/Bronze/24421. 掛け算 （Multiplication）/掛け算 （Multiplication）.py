from itertools import combinations as comb

n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in comb(range(n), 3):
    if a[i[0]] * a[i[1]] == a[i[2]]:
        ans += 1

print(ans)
