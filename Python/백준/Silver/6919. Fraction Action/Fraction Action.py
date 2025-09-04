from fractions import Fraction as f

n = int(input())
m = int(input())

v = f(n, m)
if v.numerator > v.denominator and v.denominator != 1:
    print(n // m, f(n % m, m))
else:
    print(v)