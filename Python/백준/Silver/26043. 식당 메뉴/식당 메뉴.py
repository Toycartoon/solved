import sys
from collections import deque

input = sys.stdin.readline

a = []
b = []
c = deque()
for i in range(int(input())):
    com, x, *y = map(int, input().split())
    if com == 1:
        c.append((x, y[0]))
    elif com == 2:
        n, luv = c.popleft()
        if luv == x:
            a.append(n)
        else:
            b.append(n)

a.sort()
b.sort()
c = sorted(list(c), key=lambda x: (x[0]))
print(*a if len(a) > 0 else ["None"])
print(*b if len(b) > 0 else ["None"])
if len(c) == 0:
    print("None")
else:
    for i in c:
        print(i[0], end=" ")
