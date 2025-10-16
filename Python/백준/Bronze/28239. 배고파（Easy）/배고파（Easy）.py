from math import log2

for n in range(int(input())):
    m = int(input())
    for x in range(int(log2(m))+1):
        for y in range(x, int(log2(m))+1):
            if 2 ** x + 2 ** y == m:
                print(x, y)
