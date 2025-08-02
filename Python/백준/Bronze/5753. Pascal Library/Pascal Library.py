import sys

input = sys.stdin.readline

while True:
    n, d = map(int, input().split())
    if n == d == 0:
        break

    f = False
    a = [list(map(int, input().split())) for _ in range(d)]
    for i in zip(*a):
        if i.count(1) == d:
            f = True
            break

    if f:
        print("yes")
    else:
        print("no")
