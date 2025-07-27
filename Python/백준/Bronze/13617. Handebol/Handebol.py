n, m = map(int, input().split())
ans = 0
for i in range(n):
    x = list(map(int, input().split()))
    if x.count(0) == 0:
        ans += 1

print(ans)
