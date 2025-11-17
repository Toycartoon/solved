from decimal import Decimal as d

n, m = input().split()
if d(n) * d("0.81") <= d(m):
    print("yaho")
else:
    print("no")
