import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    a = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append((x, y))

    s = set()
    for i in range(int(input())):
        x, y = map(int, input().split())
        for dx, dy in a:
            if x-50 <= dx <= x+50 and y-50 <= dy <= y+50 and (dx, dy) not in s:
                s.add((dx, dy))
    print(len(s))
