import sys

input = sys.stdin.readline

for i in range(int(input())):
    k = int(input())
    x = 0
    while True:
        if 5 ** (x-1) < k <= 5 ** x:
            break
        x += 1

    if x <= 1:
        print("MIT time")
    else:
        print(f"MIT^{x} time")
