import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = []
for i in range(m):
    a.append(int(input()))
a = a[::-1]

s = set()
v = []
for i in a:
    if i not in s:
        s.add(i)
        v.append(i)

for i in range(1, n+1):
    if i not in s:
        v.append(i)

for i in v:
    print(i)
