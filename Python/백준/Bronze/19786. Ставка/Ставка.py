import sys

input = sys.stdin.readline

for t in range(int(input())):
    a, c = map(int, input().split())
    r, g, b = map(int, input().split())

    x = a * ((r+1) ** 2 + g ** 2 + b ** 2) + c * min(r+1, g, b)
    y = a * (r ** 2 + (g+1) ** 2 + b ** 2) + c * min(r, g+1, b)
    z = a * (r ** 2 + g ** 2 + (b+1) ** 2) + c * min(r, g, b+1)
    if max(x, y, z) == x:
        print("RED")
    elif max(x, y, z) == y:
        print("GREEN")
    else:
        print("BLUE")
