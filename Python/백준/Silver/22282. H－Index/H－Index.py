import sys

input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

a.sort()
for i in range(n, -1, -1):
    if i <= a[-i]:
        print(i)
        break
