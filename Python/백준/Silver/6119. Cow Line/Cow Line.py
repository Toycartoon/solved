from collections import deque
import sys

input = sys.stdin.readline

q = deque()
v = 1
for i in range(int(input())):
    com, arr, *n = input().strip().split()

    if com == "A":
        if arr == "L":
            q.appendleft(v)
        elif arr == "R":
            q.append(v)
        v += 1
    elif com == "D":
        if arr == "L":
            for _ in range(int(n[0])):
                q.popleft()
        elif arr == "R":
            for _ in range(int(n[0])):
                q.pop()

for i in q:
    print(i)
