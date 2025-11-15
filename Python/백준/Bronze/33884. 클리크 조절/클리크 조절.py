import sys

input = sys.stdin.readline

a = []
b = []
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    a.append((x, y))

for j in range(n):
    x, y = map(int, input().split())
    b.append((x, y))
a.sort()
b.sort()
print(b[0][0]-a[0][0], b[0][1]-a[0][1])
