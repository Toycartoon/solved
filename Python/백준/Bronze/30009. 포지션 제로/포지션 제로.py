n = int(input())
x, y, r = map(int, input().split())
a, b = 0, 0

for t in range(n):
    v = int(input())

    if x - r < v < x + r:
        a += 1
    elif x - r == v or x + r == v:
        b += 1

print(a, b)
