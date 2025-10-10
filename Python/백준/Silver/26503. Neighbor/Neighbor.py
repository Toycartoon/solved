from fractions import Fraction as f

for t in range(int(input())):
    a, b, c, d = map(int, input().split())
    v = abs(f(a, b)-f(c, d))
    if v.numerator == 1:
        print(v)
    else:
        print("NOT NEIGHBORS")
