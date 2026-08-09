import sys
from math import inf
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
a = [[*input()] for _ in range(n)]
visited = [[inf for _ in range(m)] for __ in range(n)]

q = deque()
def bfs(_x, _y):
    global chunggukjang, sushi, mac_n_cheese

    pos = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    visited[_y][_x] = 0
    q.append((_x, _y))

    while q:
        x, y = q.popleft()

        for dx, dy in pos:
            if 0 <= x+dx < m and 0 <= y+dy < n:
                if visited[y+dy][x+dx] == inf and a[y+dy][x+dx] != "1":
                    visited[y+dy][x+dx] = visited[y][x] + 1
                    q.append((x+dx, y+dy))

                    if a[y+dy][x+dx] == "3":
                        chunggukjang = visited[y+dy][x+dx]
                    elif a[y+dy][x+dx] == "4":
                        sushi = visited[y+dy][x+dx]
                    elif a[y+dy][x+dx] == "5":
                        mac_n_cheese = visited[y+dy][x+dx]


chunggukjang = inf
sushi = inf
mac_n_cheese = inf
bird = (inf, inf)
for y in range(n):
    for x in range(m):
        if a[y][x] == "2":
            bird = (x, y)
            break

bfs(*bird)
if chunggukjang == sushi == mac_n_cheese == inf:
    print("NIE")
else:
    print("TAK")
    print(min(chunggukjang, sushi, mac_n_cheese))
