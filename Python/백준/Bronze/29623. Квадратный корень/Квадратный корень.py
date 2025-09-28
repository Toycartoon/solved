from decimal import Decimal

for t in range(int(input())):
    a, b, c, d = input().split()
    l = Decimal(a) + Decimal(b) ** Decimal("0.5")
    r = Decimal(c) + Decimal(d) ** Decimal("0.5")
    
    if l > r:
        print("Greater")
    elif l < r:
        print("Less")
    else:
        print("Equal")
