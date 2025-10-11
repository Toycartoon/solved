from collections import deque

s = int(input())
q = deque(range(1, 9))
q.rotate(-s+1)

visited = [0 for _ in range(9)]
visited[q[0]] = 1

print(q[0], end=" ")
while True:
    a = input()
    if a == "#":
        break
    if a[0] == "A":
        q.rotate(int(a[1]))
    elif a[0] == "C":
        q.rotate(-int(a[1]))

    print(q[0], end=" ")
    visited[q[0]] += 1
print("reject" if max(visited) >= 2 or visited.count(1) < 5 else "")
