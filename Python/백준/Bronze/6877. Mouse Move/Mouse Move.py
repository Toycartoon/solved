r, c = map(int, input().split())
x, y = 0, 0
while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    if a < 0:
        x = max(0, x+a)
    else:
        x = min(r, x+a)

    if b < 0:
        y = max(0, y+b)
    else:
        y = min(c, y+b)
    print(x, y)
