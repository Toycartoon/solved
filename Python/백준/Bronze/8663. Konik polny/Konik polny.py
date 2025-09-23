x, s = map(int, input().split())
ans = 0
while x > 0 and s > 1:
    ans += 1
    x -= s
    s = max(1, s // 2)

if x <= 0:
    print(ans)
else:
    print(ans + x)
