from math import log10

for t in range(int(input())):
    h, _, n = input().split()
    if h == "H":
        print(f"{-log10(float(n)):.02f}")
    else:
        print(f"{14+log10(float(n)):.02f}")
