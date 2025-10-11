from itertools import product as prod

a, b, c = map(int, input().split())
ans = float('inf')

for op1, op2 in prod([*"+-*/"], repeat=2):
    if op1 == "/":
        if a % b == 0:
            v = a // b
        else:
            continue
    else:
        v = eval(f"{a}{op1}{b}")
    if op2 == "/":
        if v % c == 0:
            final = min(ans, v // c)
        else:
            continue
    else:
        final = eval(f"{v}{op2}{c}")

    if final >= 0:
        ans = min(ans, final)
print(ans)
