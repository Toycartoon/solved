n = int(input())
l, r = 0, 1

s = 1
ans = 0
while r <= n:
    if s < n:
        r += 1
        s += r
    elif s > n:
        s -= l
        l += 1
    else:
        ans += 1
        r += 1
        s += r

print(ans)
