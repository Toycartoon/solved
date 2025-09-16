from math import trunc

v = 0
n = int(input())
for t in range(n):
    q = input().replace("0", "9").replace("6", "9")
    if len(q) == 3:
        v += 100
    else:
        v += int(q)

print(trunc(v / n + 0.5))
