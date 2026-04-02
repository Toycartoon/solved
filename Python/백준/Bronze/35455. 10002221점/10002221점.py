from decimal import Decimal as d

for t in range(int(input())):
    n, s = map(int, input().split())
    x = d(str(10 ** 7)) / d(str((2 * n)))
    if (d("2") * x + d("1")) * d(str(n)) == s:
        print("Yes")
    else:
        print("No")
