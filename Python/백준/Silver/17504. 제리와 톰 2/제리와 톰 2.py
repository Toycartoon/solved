from fractions import Fraction as frac

n = int(input())
a = list(map(int, input().split()))

v = frac(1, a[-1])
for i in range(n-2, -1, -1):
    v = frac(1, a[i] + v)
print((1-v).numerator, (1-v).denominator)
