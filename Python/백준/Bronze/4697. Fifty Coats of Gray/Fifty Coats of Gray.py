from math import ceil

while True:
    n, width, length, height, area, m = map(int, input().split())

    if n == width == length == height == area == m == 0:
        break

    a = n * ((width * length) + 2 * (width * height) + 2 * (length * height))
    for i in range(m):
        w, h = map(int, input().split())
        a -= w * h * n

    print(ceil(a / area))
