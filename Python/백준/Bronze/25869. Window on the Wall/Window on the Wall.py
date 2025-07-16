w, h, d = map(int, input().split())
if min(w - 2 * d, h - 2 * d) <= 0:
    print(0)
else:
    print((w - 2 * d) * (h - 2 * d))
