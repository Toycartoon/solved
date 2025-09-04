from fractions import Fraction as f

for t in range(int(input())):
    n, a, b, c = map(int, input().split())
    v = f((a * b * c - a * b - b * c - a * c) * n, a * b + b * c + a * c)
    if v.numerator < 0 or v.numerator % v.denominator != 0:
        print(-1)
    else:
        k = v.numerator // v.denominator
        if (n+k) % a != 0 or (n+k) % b != 0 or (n+k) % c != 0:
            print(-1)
        else:
            print(k)
