from math import log2

n = int(input())
print(64 - int(log2(pow(2, 64) - n)))
