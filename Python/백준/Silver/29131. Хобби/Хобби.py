import sys

input = sys.stdin.readline

a = []
for i in range(int(input())):
    x, y = map(int, input().split())
    a.append((x, y, i+1))

a.sort()
print(len(a) // 2)
for i in range(1, len(a), 2):
    print(a[i-1][2], a[i][2])
