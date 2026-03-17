import sys

input = sys.stdin.readline

n = int(input())
d = list(map(int, input().split()))

for q in range(int(input())):
    com, c, *x = map(int, input().split())

    if com == 1:
        s = x[0]
        for i in range(c-1, -1, -1):
            v = min(d[i], s)
            d[i] += v
            s -= v
            if s <= 0:
                break

        s = x[0]
        for i in range(c, n):
            v = min(d[i], s)
            d[i] += v
            s -= v
            if s <= 0:
                break
    elif com == 2:
        print(d[c-1])
