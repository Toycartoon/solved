while True:
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == y1 == x2 == y2 == 0:
        break

    x = x2-x1
    y = y2-y1
    if x == y == 0:
        print(0)
    elif x == 0 or y == 0 or x == y or x + y == 0:
        print(1)
    else:
        print(2)
