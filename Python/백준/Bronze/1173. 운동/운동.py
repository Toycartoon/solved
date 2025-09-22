n, mn, mx, t, r = map(int, input().split())
ans = 0
x = mn
if mn + t > mx:
    print(-1)
    exit()

while n > 0:
    if x + t <= mx:
        x += t
        n -= 1
    else:
        x = max(mn, x - r)
    ans += 1

print(ans)
