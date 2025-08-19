from collections import deque

n, k = map(int, input().split())
q = deque(range(1, n+1))

s = input()
for i in s:
    if i == "A":
        q.rotate(-1)
    elif i == "B":
        v = q.popleft()
        q.rotate(-1)
        q.appendleft(v)

print(q.popleft())
