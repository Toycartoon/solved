from decimal import Decimal as d

n = int(input())
s = d(input()[1:])

ans = 0
for i in range(n):
    v = d(input()[1:])
    s += v
    if int(s) != s:
        ans += 1
print(ans)
