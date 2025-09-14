from decimal import Decimal as d
from math import trunc

n, m, s = input().split()
print(min(trunc(d(s) * (d(m) + d('1')) - (d(s) * (d(m) + d("1")) * (d(n) / d("100")))), d(s) * d(m)))