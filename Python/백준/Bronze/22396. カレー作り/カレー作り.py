from math import ceil

while True:
    r0, w0, c, r = map(int, input().split())
    if r0 == w0 == c == r == 0:
        break
    print(max(0, ceil((c * w0 - r0) / r)))
