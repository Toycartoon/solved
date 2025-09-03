from fractions import Fraction as f

n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in a:
    ans += f(1, i)
print(f(1, ans), "/1" if "/" not in str(f(1, ans)) else "", sep="")
