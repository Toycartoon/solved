import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())

    f = True
    for i in range(2, n+1):
        if (n+1) % i == 0:
            f = False
            break

    if f:
        print(1)
        print(1, n+1)
    else:
        print(0)
