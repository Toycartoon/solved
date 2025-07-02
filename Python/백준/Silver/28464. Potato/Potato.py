from collections import deque

n = int(input())
a = deque(sorted(map(int, input().split())))

s, p = 0, 0
while a:
    p += a.pop()
    s += a.popleft() if len(a) else 0

print(s, p)
