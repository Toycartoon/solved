import sys

input = sys.stdin.readline

while True:
    z = int(input())
    if z == 0:
        break

    mx = 0
    x = 1
    while x ** 3 <= z ** 3:
        y = 1
        while x ** 3 + y ** 3 <= z ** 3:
            if x ** 3 + y ** 3 <= z ** 3:
                mx = max(mx, x ** 3 + y ** 3)
            y += 1
        x += 1
    print(z**3 - mx)
