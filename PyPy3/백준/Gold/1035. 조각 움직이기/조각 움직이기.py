from collections import deque
import copy

pos = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def flood_fill(g):
    c = 0
    visited = [[False for _ in range(5)] for __ in range(5)]
    dq = deque()
    for y in range(5):
        for x in range(5):
            if g[y][x] == "*" and not visited[y][x]:
                visited[y][x] = True
                dq.append((x, y))

                while dq:
                    dx, dy = dq.popleft()

                    for wx, wy in pos:
                        if 0 <= dx + wx < 5 and 0 <= dy + wy < 5:
                            if g[dy+wy][dx+wx] == "*" and not visited[dy+wy][dx+wx]:
                                visited[dy+wy][dx+wx] = True
                                dq.append((dx+wx, dy+wy))
                c += 1

    return c == 1


def make_map(g):
    m = ""
    dir = []
    for y in range(5):
        for x in range(5):
            m += g[y][x]
            if g[y][x] == "*":
                dir.append((x, y))

    return m, dir


def bfs(init_g):
    visited = {}
    q = deque()

    m, _dir = make_map(init_g)
    visited[m] = 0

    q.append(init_g)
    while q:
        g = q.popleft()
        m, dir = make_map(g)

        if flood_fill(g):
            return visited[m]

        for x, y in dir:
            for dx, dy in pos:
                if 0 <= x+dx < 5 and 0 <= y+dy < 5:
                    if g[y+dy][x+dx] == ".":
                        new_g = copy.deepcopy(g)
                        new_g[y][x] = "."
                        new_g[y+dy][x+dx] = "*"

                        _m, _dir = make_map(new_g)
                        if _m not in visited:
                            visited[_m] = visited[m] + 1
                            q.append(new_g)


g = [[*input()] for _ in range(5)]
print(bfs(g))
