from math import factorial as f

while True:
    a, b = map(int, input().split())
    if a == b == -1:
        break

    c = f(a + b) // (f(a) * f(b))
    if a + b == c:
        print(f"{a}+{b}={a+b}")
    else:
        print(f"{a}+{b}!={a+b}")
