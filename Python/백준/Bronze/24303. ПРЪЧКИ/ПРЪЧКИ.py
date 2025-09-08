from math import ceil

a1, a2, a3, b1, b2, b3, l = map(int, input().split())
a = [(a1, b1), (a2, b2), (a3, b3)]
ans = 0
a.sort(key=lambda x: -x[0])
for x, y in a:
    if x * y >= l:
        ans += ceil(l / x)
        l = 0
        break
    else:
        l -= x * y
        ans += y

print(ans if l <= 0 else 0)
