from math import lcm

n = int("".join(input().split(".")))
print(lcm(n, 36000) // n)
