import sys
from math import lcm

input = sys.stdin.readline

a = []
for i in range(int(input())):
    a.append(int(input()))
print(lcm(*a))
