from fractions import Fraction as f
import sys

input = sys.stdin.readline

t = 1
while True:
    n = int(input())
    if n == 0:
        break

    a = 0
    for i in range(n):
        w, *d = input().strip().split("/")
        if len(d) == 0:
            d = "1"

        if "," in w:
            x, y = w.split(',')
            a += f(int(x) * int(d[0]) + int(y), int(d[0]))
        else:
            a += f(int(w), int(d[0]))

    if a.denominator == 1 or a.numerator < a.denominator:
        print(f"Test {t}: {a}")
    else:
        print(f"Test {t}: {a.numerator//a.denominator},{a.numerator%a.denominator}/{a.denominator}")
    t += 1