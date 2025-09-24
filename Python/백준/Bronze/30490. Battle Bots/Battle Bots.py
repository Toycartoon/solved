from decimal import Decimal as d

n = d(input())
ans = 0
while n > 1:
    ans += 1
    n = n / d('2')
print(ans + 1)
