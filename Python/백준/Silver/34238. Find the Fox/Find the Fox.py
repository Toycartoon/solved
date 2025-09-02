import sys

input = sys.stdin.readline

n, m = map(int, input().split())
g = [[*input()] for _ in range(n)]

ans = 0
for y in range(n):
    for x in range(m):
        if g[y][x] == "F":
            if y >= 2 and g[y-1][x] == "O" and g[y-2][x] == "X":
                ans += 1
            if y >= 2 and x < m-2 and g[y-1][x+1] == "O" and g[y-2][x+2] == "X":
                ans += 1
            if x < m-2 and g[y][x+1] == "O" and g[y][x+2] == "X":
                ans += 1
            if y < n-2 and x < m-2 and g[y+1][x+1] == "O" and g[y+2][x+2] == "X":
                ans += 1
            if y < n-2 and g[y+1][x] == "O" and g[y+2][x] == "X":
                ans += 1
            if y < n-2 and x >= 2 and g[y+1][x-1] == "O" and g[y+2][x-2] == "X":
                ans += 1
            if x >= 2 and g[y][x-1] == "O" and g[y][x-2] == "X":
                ans += 1
            if y >= 2 and x >= 2 and g[y-1][x-1] == "O" and g[y-2][x-2] == "X":
                ans += 1

print(ans)
