import sys

input = sys.stdin.readline

v = []
for i in range(int(input())):
    x, a, b, c, d = map(int, input().split())
    v.append((a, b, c, d, x))

for i in range(4):
    v.sort(key=lambda x: (x[i], -x[-1]))
    print(v[-1][-1], end=" ")
    v.pop()
