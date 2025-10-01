from math import trunc
from decimal import Decimal as d

while True:
    try:
        s = input().split()
        print(f"{' '.join(s)}: {trunc((d(s[1]) / d("1000") * d(s[3]) * d("2") + d(s[-1]) * d("2.54")) * d("3.141592") + d("0.5"))}")
    except EOFError:
        break
