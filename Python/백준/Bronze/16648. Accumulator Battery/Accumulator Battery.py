t, p = map(int, input().split())
if p > 20:
    x = t / (100 - p)
    print((p-20) * x + 20 * 2 * x)
else:
    x = t / ((20 - p) * 2 + 80)
    print(p * 2 * x)
