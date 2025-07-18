n, t = map(int, input().split())

ans = 1
x = 1
f = False
while x < t:
    if not f:
        ans += 1
        if ans == 2 * n:
            f = not f
    else:
        ans -= 1
        if ans == 1:
            f = not f
    x += 1

print(ans)
