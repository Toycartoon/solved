from decimal import Decimal as d

t, r, v = input().split()
print(max(0, d(v)-d("2") * d(r) / d(t)))
