import sys

input = sys.stdin.readline

while True:
    n, *p = input().strip().split("   ")
    if n == "0":
        break

    while len(p) < int(n):
        p.extend(input().strip().split("   "))

    x1, y1 = map(float, p[0].split())
    l = [(x1, y1)]

    for i in range(1, len(p)):
        x, y = map(float, p[i].split())
        l.append((x, y))

    l.append((x1, y1))


    s = 0
    for i in range(int(n)):
        s += l[i][0] * l[i+1][1]

    for i in range(int(n)):
        s -= l[i][1] * l[i+1][0]

    print(round(abs(s * 0.5)))
