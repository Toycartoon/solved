l, h = map(int, input().split())
ans = 0
for c in range(l, h+1):
    if len({*str(c)}-{"0"}) != 6:
        continue

    f = True
    for i in str(c):
        if c % int(i) != 0:
            f = False
            break

    if f:
        ans += 1
print(ans)
