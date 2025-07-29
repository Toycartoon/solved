from decimal import Decimal as d

for t in range(int(input())):
    x1, y1, z1 = input().split()
    x2, y2, z2 = input().split()

    a = d(x1) * d(y2) + d(y1) * d(z2) + d(z1) * d(x2)
    g = d(x2) * d(y1) + d(y2) * d(z1) + d(z2) * d(x1)

    if a > g:
        print("ADAM")
    elif a < g:
        print("GOSIA")
    else:
        print("=")
