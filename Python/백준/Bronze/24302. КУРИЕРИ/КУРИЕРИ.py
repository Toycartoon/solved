def f(x):
    if x <= 5:
        i = 4
    elif x <= 10:
        i = 7
    elif x <= 20:
        i = 12
    elif x <= 30:
        i = 17
    else:
        i = x * 0.57

    if x <= 2:
        j = x * 0.9 + 0.9
    elif x <= 5:
        j = 1 + x * 0.85
    elif x <= 20:
        j = 1.25 + x * 0.8
    elif x <= 40:
        j = 3.25 + x * 0.7
    else:
        j = 9.25 + x * 0.55

    return min(i, j)

a, b = map(int, input().split())
print(f"{f(a // 1000) + f(b // 1000):.02f}")
