import sys

input = sys.stdin.readline

a = []
for i in range(int(input())):
    q, p = map(int, input().split())
    a.append((q, p))

a.sort(key=lambda x: (-x[0], x[1]))
print(*a[0], *a[1])

a.sort(key=lambda x: (x[1], -x[0]))
print(*a[0], *a[1])
