a, b = map(int, input().split())
plus, minus, mul = a + b, a - b, a * b

if plus > minus and plus > mul:
    if a < 0:
        a = "(" + str(a) + ")"
    if b < 0:
        b = "(" + str(b) + ")"
    if plus < 0:
        plus = "(" + str(plus) + ")"
    print(f"{a}+{b}={plus}")
elif minus > plus and minus > mul:
    if a < 0:
        a = "(" + str(a) + ")"
    if b < 0:
        b = "(" + str(b) + ")"
    if minus < 0:
        minus = "(" + str(minus) + ")"
    print(f"{a}-{b}={minus}")
elif mul > plus and mul > minus:
    if a < 0:
        a = "(" + str(a) + ")"
    if b < 0:
        b = "(" + str(b) + ")"
    if mul < 0:
        mul = "(" + str(mul) + ")"
    print(f"{a}*{b}={mul}")
else:
    print("NIE")
