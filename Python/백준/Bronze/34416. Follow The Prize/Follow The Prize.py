import sys

input = sys.stdin.readline

c = [False for _ in range(int(input())+1)]
n = int(input())
c[n] = True
for q in range(int(input())):
    a, b = map(int, input().split())
    c[a], c[b] = c[b], c[a]
print(c.index(True))
