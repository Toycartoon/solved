from math import lcm

n = int(input())
t = list(map(int, input().split()))
print(lcm(*t))
