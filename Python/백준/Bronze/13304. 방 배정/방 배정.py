from math import ceil

_12 = 0
m34 = 0
w34 = 0
m56 = 0
w56 = 0
n, k = map(int, input().split())
for i in range(n):
    g, a = map(int, input().split())
    if 1 <= a <= 2:
        _12 += 1
    elif 3 <= a <= 4:
        if g == 0:
            w34 += 1
        elif g == 1:
            m34 += 1
    elif 5 <= a <= 6:
        if g == 0:
            w56 += 1
        elif g == 1:
            m56 += 1
print(ceil(_12 / k) + ceil(w34 / k) + ceil(m34 / k) + ceil(m56 / k) + ceil(w56 / k))
