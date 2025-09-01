import sys

input = sys.stdin.readline

x = 0
for i in range(int(input())):
    p, c = map(int, input().split())
    if abs(p-x) <= c:
        x += 1
print(x)
