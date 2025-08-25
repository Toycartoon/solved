from math import ceil

s = input()
u = s.count("U") + s.count("C")
dp = s.count("D") + s.count("P")
print("U" if u > ceil(dp / 2) else "", end="")
print("DP" if dp != 0 else "")
