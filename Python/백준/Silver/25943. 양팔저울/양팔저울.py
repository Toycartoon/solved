n = int(input())
a = list(map(int, input().split()))

l, r = a[0], a[1]
for i in range(2, n):
    if l <= r:
        l += a[i]
    else:
        r += a[i]

w = abs(l-r)
v = [100, 50, 20, 10, 5, 2, 1]
ans = 0
for i in v:
    if w // i > 0:
        ans += w // i
        w %= i

print(ans)
