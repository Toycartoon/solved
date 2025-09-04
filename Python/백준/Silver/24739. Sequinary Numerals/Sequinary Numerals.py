from fractions import Fraction as f

d = input()[::-1]
ans = 0
for i in range(len(d)):
    ans += int(d[i]) * (f(3, 2) ** i)

nume, deno = ans.numerator, ans.denominator
if nume >= deno and deno != 1:
    print(nume // deno, f"{nume % deno}/{deno}")
else:
    print(ans)