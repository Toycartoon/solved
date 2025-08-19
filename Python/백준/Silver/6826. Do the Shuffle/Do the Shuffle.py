from collections import deque
import sys

input = sys.stdin.readline

q = deque(["A", "B", "C", "D", "E"])
while True:
    b = int(input())
    n = int(input())

    if b == 1:
        q.rotate(-n)
    elif b == 2:
        q.rotate(n)
    elif b == 3:
        if n % 2 == 1:
            q[1], q[0] = q[0], q[1]
    elif b == 4:
        break

print(*q)
