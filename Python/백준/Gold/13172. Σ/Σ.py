from fractions import Fraction as f

ans = f(0, 1)
for i in range(int(input())):
    n, s = map(int, input().split())
    ans += f(s, n)
print(ans.numerator * pow(ans.denominator, -1, 1000000007) % 1000000007)
