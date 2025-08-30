x, y = map(int, input().split())
r = int(input())
for dx, dy in [(1, 1), (1, -1), (-1, -1), (-1, 1)]:
    print(x+dx*r, y+dy*r)
