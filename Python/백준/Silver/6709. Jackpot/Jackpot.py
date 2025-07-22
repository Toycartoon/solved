from math import lcm

for t in range(int(input())):
    w = int(input())
    a = lcm(*map(int, input().split()))
    print(a if a <= 10 ** 9 else 'More than a billion.')
