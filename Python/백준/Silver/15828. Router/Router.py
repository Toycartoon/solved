from collections import deque
import sys

input = sys.stdin.readline

q = deque()
size = int(input())
while True:
    n = int(input())
    if n == -1:
        break

    if n == 0:
        q.popleft()
    else:
        if len(q) + 1 <= size:
            q.append(n)

if q:
    print(*q)
else:
    print("empty")
