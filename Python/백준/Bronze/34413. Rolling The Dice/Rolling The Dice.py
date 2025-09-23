xy, z = input().split("+")
x, y = map(int, xy.split("d"))
if (x + x * y) % 2 == 0:
    print((x + x * y) // 2 + int(z))
else:
    print((x + x * y) / 2 + int(z))
