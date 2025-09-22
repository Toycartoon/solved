from collections import deque

q = deque()
def bfs(n):
    q.append(n)
    while q:
        x = q.popleft()
        if x % t == 0:
            return x
        q.append(x * 10)
        q.append(x * 10 + 1)

for i in range(int(input())):
    t = int(input())
    print(bfs(1))
    q.clear()
