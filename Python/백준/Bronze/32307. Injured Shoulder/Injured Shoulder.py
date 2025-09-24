import sys
from itertools import product as prod

input = sys.stdin.readline

n = int(input())
w = set()
for i in range(n):
    w.add(input().strip())

for i in range(int(input())):
    s = input().strip()
    if s in w:
        print(1)
        continue

    f = False
    for v in prod(w, repeat=2):
        if v[0]+v[1] == s:
            f = True
            break

    if f:
        print(2)
    else:
        print(0)
