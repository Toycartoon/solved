from fractions import Fraction as f

h = int(input())
ans = 0
for i in range(1, h+1):
    ans += f(1, i)

print(ans.numerator)
print(ans.denominator)