import sys

input = sys.stdin.readline

n = int(input())
a = []
v = 0
for i in range(n):
    s, t = map(int, input().split())
    if s > t:
        v += 1
    else:
        a.append(v)
        v = 0

a.append(v)
print(max(a))
