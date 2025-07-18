l1, r1, l2, r2, k = map(int, input().split())
ans = 0

for i in range(l1, r1+1):
    if l2 <= i <= r2 and i != k:
        ans += 1

print(ans)
