from math import lcm
import sys

input = sys.stdin.readline

a = []
for i in range(int(input())):
    a.append(int(input()))

l = lcm(*a)
for i in a:
    print(l // i)