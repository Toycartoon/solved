import sys

input = sys.stdin.readline

w = {}
for i in range(int(input())):
    x, c = input().strip().split()
    w[x] = int(c)

n = int(input())
a = -n * 10
for i in range(n):
    s = input().strip()
    if s in w:
        a += w[s]
print(a)
