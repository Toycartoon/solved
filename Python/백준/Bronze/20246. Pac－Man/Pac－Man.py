x, y = map(int, input().split())
if x != 0 and y != 0:
    for i in range(x, -1, -1):
        print(i, y)
    for i in range(y-1, 0, -1):
        print(0, i)
elif x != 0:
    for i in range(x, 0, -1):
        print(i, 0)
elif y != 0:
    for i in range(y, 0, -1):
        print(0, i)

for y in range(10):
    if y % 2 == 0:
        for x in range(10):
            print(x, y)
    else:
        for x in range(9, -1, -1):
            print(x, y)
