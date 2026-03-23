n, l = map(int, input().split())
a = []
for i in range(n):
    d, r, g = map(int, input().split())
    a.append((d, r, g))

ans = 0
dis = 0
for d, r, g in a:
    ans += d-dis
    dis += d-dis
    if ans % (r+g) > r:
        continue
    else:
        ans += r - (ans % (r+g))
ans += l - dis
print(ans)
