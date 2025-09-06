import sys

input = sys.stdin.readline

a = []
n = int(input())
for i in range(n):
    a.append(input().strip())

for i in range(1, 101):
    s = set()
    for v in range(n):
        s.add(a[v][-i:])

    if len(s) == n:
        print(i)
        break
