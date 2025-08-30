import sys

input = sys.stdin.readline

for t in range(int(input())):
    a, b, c = map(int, input().split())

    if c // 2 <= b:
        c %= 2
        if a >= c:
            print("YES")
        else:
            print("NO")
    else:
        c -= b * 2
        if a >= c:
            print("YES")
        else:
            print("NO")
