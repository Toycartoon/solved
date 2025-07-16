import sys

input = sys.stdin.readline

while True:
    p1, p2 = input().strip().split()
    s1, s2 = 0, 0

    if p1 == p2 == "#":
        break

    for i in range(int(input())):
        a, b = input().strip().split()

        if a == b:
            s1 += 1
        else:
            s2 += 1

    print(p1, s1, p2, s2)
