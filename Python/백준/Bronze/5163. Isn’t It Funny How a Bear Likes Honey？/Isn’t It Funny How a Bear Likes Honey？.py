from math import pi
import sys

input = sys.stdin.readline

for t in range(int(input())):
    b, w = map(float, input().split())
    k = 0
    for i in range(int(b)):
        r = float(input())
        k += (4 / 3) * pi * pow(r, 3)

    print(f"Data Set {t+1}:")
    print("Yes" if k / 1000 >= w else "No")
    print()
