import sys

input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break

    x, y = map(int, input().split())
    for i in range(n):
        a, b = map(int, input().split())
        if a == x or y == b:
            print("divisa")
        else:
            if b > y:
                if a < x:
                    print("NO")
                else:
                    print("NE")
            else:
                if a < x:
                    print("SO")
                else:
                    print("SE")
