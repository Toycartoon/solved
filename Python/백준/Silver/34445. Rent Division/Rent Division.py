import sys
from math import ceil

input = sys.stdin.readline

a = []
s = 0
for i in range(int(input())):
    n = int(input())
    a.append(n)
    s += n

r = int(input())
v = (r + s) / len(a)
output = []
f = True
for i in a:
    if v - i <= -1:
        f = False
        break
    output.append(ceil(v - i))

if f:
    for i in output:
        print(i)
else:
    print("not possible")
